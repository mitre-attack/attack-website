"""Resolve data-driven matrix pages with optional presentation overrides."""

import re
from collections.abc import Collection, Mapping, Sequence
from copy import deepcopy
from html import escape
from typing import Any

from modules.util.buildhelpers import filter_deprecated_revoked, filter_out_subtechniques


def _matches_platforms(technique: Mapping[str, Any], platforms: Collection[str]) -> bool:
    """Return whether a technique matches the platform filter."""
    return not platforms or bool(set(platforms) & set(technique.get("x_mitre_platforms", [])))


def select_matrix_techniques(
    techniques: Sequence[Mapping[str, Any]],
    platforms: Collection[str],
    subtechniques_of: Mapping[str, Sequence[Mapping[str, Mapping[str, Any]]]],
) -> list[Mapping[str, Any]]:
    """Select active parents, retaining containers for matching active children."""
    return [
        technique
        for technique in filter_out_subtechniques(filter_deprecated_revoked(techniques))
        if (
            _matches_platforms(technique, platforms)
            or any(
                _matches_platforms(child, platforms)
                for child in filter_deprecated_revoked(
                    [child["object"] for child in subtechniques_of.get(technique["id"], [])]
                )
            )
        )
    ]


def _register_path(matrix: dict[str, Any], paths: set[str], page_keys: set[str]) -> None:
    """Register a matrix path, rejecting duplicate paths and page keys."""
    path = matrix["path"]
    # Pelican slugs and intermediate filenames flatten path separators.
    page_key = "-".join(re.sub(r"[/._]", "-", path).lower().split())
    if path in paths or page_key in page_keys:
        raise ValueError(f"Conflicting matrix path: {path}. Configure a unique platform path override.")
    paths.add(path)
    page_keys.add(page_key)


def _resolve_children(parent: dict[str, Any], platforms: set[str], links: dict[str, str]) -> None:
    """Prune inactive platform overrides and collect their platform links."""
    children = []
    for child in parent["subtypes"]:
        if child["subtypes"]:
            _resolve_children(child, platforms, links)
            child["platforms"] = [p for p in child["platforms"] if p in platforms]
            if not child["subtypes"]:
                continue
        else:
            if not set(child["platforms"]) & platforms:
                continue
            for platform in child["platforms"]:
                links[platform] = child["path"]
        children.append(child)
    parent["subtypes"] = children


def _attach_links(matrix: dict[str, Any], links: Mapping[str, str], paths: set[str], page_keys: set[str]) -> None:
    """Attach platform links and validate paths throughout a matrix tree."""
    _register_path(matrix, paths, page_keys)
    matrix["platform_links"] = [{"name": p, "path": links[p]} for p in matrix["platforms"]]
    for child in matrix["subtypes"]:
        _attach_links(child, links, paths, page_keys)


def _platform_sort_key(platform: str) -> tuple[str, str]:
    """Sort platform names case insensitively with a deterministic tie breaker."""
    return platform.casefold(), platform


def resolve_matrices(
    overrides: list[dict[str, Any]], techniques_by_domain: Mapping[str, Sequence[Mapping[str, Any]]]
) -> list[dict[str, Any]]:
    """Return matrix definitions and links for platforms in active techniques.

    Existing definitions supply presentation only. Unknown platforms receive a
    default path and description; domain matrices include all active techniques.
    """
    matrices = deepcopy(overrides)
    paths = set()
    page_keys = set()

    for domain in matrices:
        if domain["type"] != "local":
            continue
        platforms = {
            platform
            for technique in filter_deprecated_revoked(techniques_by_domain.get(domain["matrix"], []))
            for platform in technique.get("x_mitre_platforms", [])
            if platform not in domain.get("excluded_platforms", [])
        }
        links = {}

        _resolve_children(domain, platforms, links)
        for platform in sorted(platforms - links.keys(), key=_platform_sort_key):
            slug = re.sub(r"[^a-z0-9]+", "-", platform.lower()).strip("-")
            if not slug:
                raise ValueError(f"Cannot generate a matrix path for platform {platform!r}; configure an override.")
            path = f"{domain['path']}/{slug}"
            domain["subtypes"].append(
                {
                    "name": platform,
                    "type": "local",
                    "matrix": domain["matrix"],
                    "path": path,
                    "platforms": [platform],
                    "descr": "Below are the tactics and techniques representing the MITRE ATT&CK"
                    f"<sup>&reg;</sup> {escape(platform)} platform for {escape(domain['name'])}.",
                    "subtypes": [],
                }
            )
            links[platform] = path

        # Preserve editorial platform order, then append newly discovered platforms.
        domain["platforms"] = [p for p in domain["platforms"] if p in platforms] + sorted(
            platforms - set(domain["platforms"]), key=_platform_sort_key
        )
        domain["filter_platforms"] = []

        _attach_links(domain, links, paths, page_keys)
    return matrices
