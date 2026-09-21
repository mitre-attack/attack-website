# syntax=docker/dockerfile:1.7

FROM node:26-trixie-slim AS assets-build

ARG ATTACK_WEBSITE_OS_CA_TRUST_SETUP_COMMAND=":"

RUN apt update \
    && apt install -y --no-install-recommends ca-certificates curl \
    && sh -ec "${ATTACK_WEBSITE_OS_CA_TRUST_SETUP_COMMAND}" \
    && rm -rf /var/lib/apt/lists/*

# Install pre-built Just (official installer)
RUN curl --proto '=https' --tlsv1.2 -fsSL https://just.systems/install.sh -o /tmp/install-just.sh \
    && bash /tmp/install-just.sh --tag 1.58.0 --to /usr/local/bin \
    && rm /tmp/install-just.sh \
    && test "$(just --version)" = "just 1.58.0"

WORKDIR /src/attack-website

COPY attack-search/package*.json ./attack-search/
COPY attack-style/package*.json ./attack-style/
RUN npm --prefix attack-search ci && npm --prefix attack-style ci

COPY justfile ./
COPY attack-search/webpack.config.cjs ./attack-search/
COPY attack-search/.babelrc ./attack-search/
COPY attack-search/src ./attack-search/src
COPY attack-style/ ./attack-style/

# Regenerate the committed theme assets using the same copy commands as local builds.
RUN just build-assets


FROM python:3.13-slim-trixie AS site-base

ARG PELICAN_SITEURL=""
ARG ATTACK_WEBSITE_BANNER_ENABLED=""
ARG ATTACK_WEBSITE_BANNER_MESSAGE=""
ARG ATTACK_WEBSITE_INCLUDE_OSANO="false"
ARG ATTACK_WEBSITE_GOOGLE_ANALYTICS=""
ARG ATTACK_WEBSITE_GOOGLE_SITE_VERIFICATION=""
ARG ATTACK_WEBSITE_ATTACK_BRAND="false"
ARG ATTACK_WEBSITE_TEST_EXITSTATUS="true"
ARG ATTACK_WEBSITE_UPDATE_ATTACK_EXTRAS=""
ARG ATTACK_WEBSITE_UPDATE_ATTACK_ALL_EXTRAS="false"
ARG ATTACK_WEBSITE_GENERATE_STIX_CHANGELOG="false"
ARG ATTACK_WEBSITE_VERSION_ARCHIVE_DIR="/var/cache/attack-website/version-archives"
ARG ATTACK_WEBSITE_ATTACK_RELEASES_DIR="/var/cache/attack-website/attack-releases"
ARG ATTACK_WEBSITE_DIFF_STIX_VERSION="v19.1"
ARG ATTACK_WEBSITE_STIX_LOCATION_ENTERPRISE="https://raw.githubusercontent.com/mitre/cti/master/enterprise-attack/enterprise-attack.json"
ARG ATTACK_WEBSITE_STIX_LOCATION_MOBILE="https://raw.githubusercontent.com/mitre/cti/master/mobile-attack/mobile-attack.json"
ARG ATTACK_WEBSITE_STIX_LOCATION_ICS="https://raw.githubusercontent.com/mitre/cti/master/ics-attack/ics-attack.json"
ARG ATTACK_WEBSITE_STIX_LOCATION_PRE="https://raw.githubusercontent.com/mitre/cti/master/pre-attack/pre-attack.json"
ARG ATTACK_WEBSITE_WORKBENCH_USER=""
# `:` is the POSIX shell no-op, used when optional setup commands are not supplied.
ARG ATTACK_WEBSITE_OS_CA_TRUST_SETUP_COMMAND=":"
ARG ATTACK_WEBSITE_PYTHON_CA_TRUST_SETUP_COMMAND=":"

ENV PELICAN_SITEURL=${PELICAN_SITEURL} \
    ATTACK_WEBSITE_GOOGLE_ANALYTICS=${ATTACK_WEBSITE_GOOGLE_ANALYTICS} \
    ATTACK_WEBSITE_GOOGLE_SITE_VERIFICATION=${ATTACK_WEBSITE_GOOGLE_SITE_VERIFICATION} \
    ATTACK_WEBSITE_ATTACK_BRAND=${ATTACK_WEBSITE_ATTACK_BRAND} \
    ATTACK_WEBSITE_INCLUDE_OSANO=${ATTACK_WEBSITE_INCLUDE_OSANO} \
    ATTACK_WEBSITE_TEST_EXITSTATUS=${ATTACK_WEBSITE_TEST_EXITSTATUS} \
    ATTACK_WEBSITE_UPDATE_ATTACK_EXTRAS=${ATTACK_WEBSITE_UPDATE_ATTACK_EXTRAS} \
    ATTACK_WEBSITE_UPDATE_ATTACK_ALL_EXTRAS=${ATTACK_WEBSITE_UPDATE_ATTACK_ALL_EXTRAS} \
    ATTACK_WEBSITE_VERSION_ARCHIVE_DIR=${ATTACK_WEBSITE_VERSION_ARCHIVE_DIR} \
    ATTACK_WEBSITE_ATTACK_RELEASES_DIR=${ATTACK_WEBSITE_ATTACK_RELEASES_DIR} \
    ATTACK_WEBSITE_DIFF_STIX_VERSION=${ATTACK_WEBSITE_DIFF_STIX_VERSION} \
    ATTACK_WEBSITE_STIX_LOCATION_ENTERPRISE=${ATTACK_WEBSITE_STIX_LOCATION_ENTERPRISE} \
    ATTACK_WEBSITE_STIX_LOCATION_MOBILE=${ATTACK_WEBSITE_STIX_LOCATION_MOBILE} \
    ATTACK_WEBSITE_STIX_LOCATION_ICS=${ATTACK_WEBSITE_STIX_LOCATION_ICS} \
    ATTACK_WEBSITE_STIX_LOCATION_PRE=${ATTACK_WEBSITE_STIX_LOCATION_PRE} \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt update \
    && apt install -y --no-install-recommends ca-certificates curl git \
    && sh -ec "${ATTACK_WEBSITE_OS_CA_TRUST_SETUP_COMMAND}" \
    && rm -rf /var/lib/apt/lists/*

RUN curl --proto '=https' --tlsv1.2 -fsSL https://just.systems/install.sh -o /tmp/install-just.sh \
    && bash /tmp/install-just.sh --tag 1.58.0 --to /usr/local/bin \
    && rm /tmp/install-just.sh \
    && test "$(just --version)" = "just 1.58.0"

WORKDIR /src/attack-website

COPY requirements.txt ./
RUN python3 -m pip install --no-cache-dir wheel \
    && python3 -m pip install --no-cache-dir -r requirements.txt \
    && sh -ec "${ATTACK_WEBSITE_PYTHON_CA_TRUST_SETUP_COMMAND}"

COPY . ./

# Copy the complete staged asset set before Pelican renders and preserves the site.
COPY --from=assets-build /src/attack-website/attack-theme/static/ attack-theme/static/


FROM site-base AS website-build

# A Workbench API key is optional for local/upstream builds. When supplied as a BuildKit secret,
# it is available only to this command and is not persisted in an image layer.
RUN --mount=type=secret,id=workbench_api_key,required=false \
    --mount=type=cache,id=attack-website-artifacts-v1,target=/var/cache/attack-website,sharing=locked \
    if [ -f /run/secrets/workbench_api_key ]; then \
        export ATTACK_WEBSITE_WORKBENCH_API_KEY="$(cat /run/secrets/workbench_api_key)"; \
        export ATTACK_WEBSITE_WORKBENCH_USER; \
    fi; \
    if [ -n "${ATTACK_WEBSITE_BANNER_ENABLED}" ]; then export ATTACK_WEBSITE_BANNER_ENABLED; else unset ATTACK_WEBSITE_BANNER_ENABLED; fi; \
    if [ -n "${ATTACK_WEBSITE_BANNER_MESSAGE}" ]; then export ATTACK_WEBSITE_BANNER_MESSAGE; else unset ATTACK_WEBSITE_BANNER_MESSAGE; fi; \
    mkdir -p "${ATTACK_WEBSITE_VERSION_ARCHIVE_DIR}"; \
    set --; \
    if [ -n "${ATTACK_WEBSITE_UPDATE_ATTACK_EXTRAS}" ]; then \
        set -f; \
        for extra in ${ATTACK_WEBSITE_UPDATE_ATTACK_EXTRAS}; do \
            set -- "$@" --extras "$extra"; \
        done; \
    fi; \
    just build-website "$@" \
        --version-archive-dir "${ATTACK_WEBSITE_VERSION_ARCHIVE_DIR}"


FROM website-build AS changelog-build

RUN --mount=type=cache,id=attack-website-artifacts-v1,target=/var/cache/attack-website,sharing=locked \
    if [ "${ATTACK_WEBSITE_GENERATE_STIX_CHANGELOG}" = "true" ]; then \
        download_attack_stix --download-dir "${ATTACK_WEBSITE_ATTACK_RELEASES_DIR}" --all --stix21; \
    fi

RUN --mount=type=cache,id=attack-website-artifacts-v1,target=/var/cache/attack-website,sharing=locked \
    if [ "${ATTACK_WEBSITE_GENERATE_STIX_CHANGELOG}" = "true" ]; then \
        mkdir -p output/reports output/changes \
        && cp reports/* output/reports/ \
        && cp reports/tests.html output/ \
        && diff_stix -v \
            --old "${ATTACK_WEBSITE_ATTACK_RELEASES_DIR}/stix-2.0/${ATTACK_WEBSITE_DIFF_STIX_VERSION}/" \
            --new output/stix/ \
            --show-key \
            --contributors \
            --html-file output/changes/index.html \
            --html-file-detailed output/changes/changelog-detailed.html \
            --markdown-file output/changes/changelog.md \
            --json-file output/changes/changelog.json \
            --layers output/changes/layer-enterprise.json output/changes/layer-mobile.json output/changes/layer-ics.json; \
    fi


FROM nginx:stable-alpine AS production

COPY --from=changelog-build /src/attack-website/output /var/www/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

LABEL org.opencontainers.image.title="ATT&CK Website" \
    org.opencontainers.image.description="Static ATT&CK Website served by Nginx" \
    org.opencontainers.image.source="https://github.com/mitre-attack/attack-website" \
    org.opencontainers.image.url="https://attack.mitre.org/" \
    org.opencontainers.image.vendor="MITRE ATT&CK"

EXPOSE 80

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD wget -q -O /dev/null http://127.0.0.1/ || exit 1

CMD ["nginx", "-g", "daemon off;"]
