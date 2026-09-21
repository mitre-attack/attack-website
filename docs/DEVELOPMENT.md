# Developer guide

[Workflow 1](#workflow-1-build-and-run-using-docker) builds and serves the website in
Docker. For faster rebuilds while developing locally, use
[Workflow 2](#workflow-2-build-locally-and-serve-using-docker).

The [customization guide](CUSTOMIZING.md) explains how to change the site's style,
content, and functionality. To contribute changes, follow the
[contribution guide](CONTRIBUTING.md).
Report bugs through the [GitHub issue tracker](https://github.com/mitre-attack/attack-website/issues).
For errors or typos in site content, email <attack@mitre.org> with the subject
**Website Content Error**, a description, and the affected URL.

## Prerequisites

Docker is the only tool you need on the host for a Docker build. The build images
include Just, Node.js, Python, and their dependencies.

For local builds, install:

- [Just](https://just.systems/man/en/installation.html) 1.58.0 or newer
- [uv](https://docs.astral.sh/uv/getting-started/installation/) for Python environment
  and dependency installation
- Python 3.13
- Node.js 26 and npm to build Search and Style
- Docker

On macOS, install Just and uv with `brew install just uv`, then install Node.js 26
separately. On Windows, use WSL: the recipes and npm scripts require a POSIX shell.

## Workflow 1: Build and run using Docker

From the repository root:

```sh
docker build -t attack-website .
docker run --rm -p 80:80 attack-website
```

Open <http://localhost> to view the site. During the build, the `assets-build` stage
runs `just build-assets` to rebuild Search and Style and copy them into the theme.
The Python stage then runs `just build-website`. Nginx serves the generated site
from the final image.

See the [Docker guide](DOCKER.md) for build arguments, branding and extras,
BuildKit secrets, caches, and test-exit behavior.

## Workflow 2: Build locally and serve using Docker

From the repository root, install dependencies and build:

```sh
just install-deps
just build-full-website --attack-brand --all-extras
```

`install-deps` creates `.venv` with Python 3.13 if needed and installs
`requirements.txt` there. It also runs `npm ci` in each package directory,
`attack-search/` and `attack-style/`. If you already have a `.venv`, the command
reuses it. It leaves global Python packages alone.

Run it again when dependencies change. The build commands don't install dependencies.

Website builds use `.venv/bin/python` if it exists, or `python3` from PATH otherwise.
To use a different interpreter, set `PYTHON` to its executable path. Just also adds
that interpreter's directory to PATH so it can find tools such as Pelican. You don't
need to activate the virtual environment, and you can run Just from any repository
subdirectory.

The build copies Search and Style into the theme before generating the site in
`output/` (or its configured subdirectory). If you've only changed content, use
`just build-website --attack-brand --all-extras` to reuse the staged assets.
The flags in these examples enable branding and extras; Just leaves both opt-in.

Serve the output with the test Nginx image, still from the repository root:

```sh
docker build -t attack-website-test test/
docker run --rm -p 80:80 -v "$(pwd)/output:/workspace:ro" attack-website-test
```

Open <http://localhost>. Rebuild locally and refresh the browser to see changes.
The [test environment guide](../test/README.md) covers the helper script and server
usage. Validate with Nginx, since Pelican's built-in development server handles
routing differently from production.

## Commands and generator options

Run `just` or `just --list` to list commands.

| Command | Behavior |
| --- | --- |
| `just install-deps` | Install Python and both npm packages' dependencies |
| `just build-search` | Compile and stage the production Search bundle |
| `just build-style` | Compile and stage all three stylesheets |
| `just build-assets` | Compile and stage both Search and Style |
| `just build-website` | Generate the website using existing staged assets |
| `just build-full-website` | Rebuild both asset sets, then generate the website |

Both website commands use the defaults from `update-attack.py`, so branding and
optional modules remain opt-in. Add generator options after the command. You don't
need an extra `--` separator:

```sh
just build-website --attack-brand --all-extras
just build-full-website --attack-brand --extras resources --extras blog
just build-website --banner "Preview website"
just build-website --help
```

Just passes repeated options and quoted values through unchanged.
`ATTACK_WEBSITE_*` and `PELICAN_*` environment settings also apply. The Search,
Style, and assets commands don't accept generator options. To work with individual
modules, you can also run `.venv/bin/python update-attack.py` directly.

If dependency installation, asset compilation, or website generation fails, the
command exits with a nonzero status. Failing site checks also stop the build unless
you pass `--no-test-exitstatus` or set `ATTACK_WEBSITE_TEST_EXITSTATUS=false`.
GitHub Pages explicitly overrides this behavior. Run Jest and linters separately.

## Compiled assets and developer responsibility

After changing anything in `attack-style/` or `attack-search/`, rebuild the affected
assets and commit the generated files in `attack-theme/static/` with your changes.

Use `just build-style`, `just build-search`, or `just build-assets` to regenerate
files instead of editing them by hand. Both packages also have `npm run build`,
`npm run copy`, and `npm run build-copy` commands. Just calls `build-copy`, which
copies the compiled files into the theme. These commands work before `output/`
exists and don't copy files into the live site output.

| Files | Git policy |
| --- | --- |
| `attack-style/dist/`, `attack-search/dist/` | Ignored intermediate output |
| `attack-search/compilation-stats.json` | Ignored development output |
| `attack-theme/static/style-{attack,user,archive}.css` | Committed compiled assets |
| `attack-theme/static/scripts/search_bundle.js` | Committed compiled asset |
| `attack-theme/static/scripts/settings.js` | Ignored, generated for each site build |

GitHub Pages installs Just and Python dependencies, then runs `just build-website`
using the committed assets. It doesn't install npm dependencies, rebuild bundles,
or compare them with regenerated output. You are responsible for committing
up-to-date bundles.

Before generating the website, Just checks that all four staged assets exist and
contain data. It doesn't check whether they match your source changes. The asset
and full-website commands always recompile the selected assets, even if their
source hasn't changed.

## Build order and generated search files

Search uses three kinds of generated files:

| File | Producer and inputs |
| --- | --- |
| `search_bundle.js` | Webpack compiles Search source and dependencies; it does not read generated HTML or search JSON |
| `settings.js` | Python generates deployment paths, version identity, and dataset-specific tour settings |
| `search/*.json` | Python extracts searchable data from rendered HTML and STIX metadata |

The build order is:

1. Put compiled CSS and Search in `attack-theme/static/` by rebuilding them or using
   the committed assets.
2. Python cleans generated output and prepares content and runtime settings.
3. Pelican renders HTML and copies the staged theme into the site.
4. Python builds search JSON, preserves the current-version snapshot when the
   `versions` extra is enabled, and runs remaining processing and site checks.

The current-version snapshot already exists by the time generation finishes, so
copying assets into live `output/` afterward won't update it. Copy them into the
theme before generation so both the live site and the snapshot receive them.
Historical archives keep their own assets.

The theme's generated `settings.js` is a separate file from
`attack-search/src/settings.js`, which Webpack compiles into the bundle. The theme
file contains `base_url`, a version-derived `build_uuid`, and dataset-dependent
`tour_steps`. Cleanup deletes it, the tour and website modules regenerate it, and
version preservation adjusts it for archived pages. Keep it ignored: its contents
apply to one dataset and deployment.
See [settings generation](../modules/website_build/website_build.py),
[tour generation](../modules/tour/tour.py), and [archive rewriting](../modules/versions/versions.py).
