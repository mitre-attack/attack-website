# AGENTS.md

This file is guidance for coding agents working in `attack-website`.

## Scope

- Applies to the repository root.
- There was no existing `AGENTS.md` to preserve.
- No Cursor rules were found in `.cursor/rules/` or `.cursorrules`.
- No Copilot instructions were found in `.github/copilot-instructions.md`.
- Primary human docs are `docs/DEVELOPMENT.md`, `README.md`, `test/README.md`, and `docs/CONTRIBUTING.md`.

## Repo Shape

- Root Python build system generates the static site via `update-attack.py`.
- `attack-search/` is a separate Node/CommonJS project for the search bundle.
- Search source and tests live in `attack-search/src/` and `attack-search/__tests__/`.
- `attack-style/` is a separate Node/Sass project for CSS output.
- SCSS entrypoints are `attack-style/style-attack.scss`, `attack-style/style-user.scss`, and `attack-style/style-archive.scss`.
- `attack-theme/` contains Jinja templates, static assets, and legacy browser JS.
- Theme templates and static assets live in `attack-theme/templates/` and `attack-theme/static/`.
- `modules/` contains Python modules that generate ATT&CK site content.
- `test/` provides an Nginx Docker environment for validating the built site.

## Environment Expectations

- Python 3 is required for the main build.
- When managing a local Python environment, prefer `uv` with a virtual environment at `.venv` in the git repository root.
- Node.js and npm are required for `attack-search/` and `attack-style/`.
- Docker is the preferred way to validate the final static output in an Nginx-like environment.
- Just `1.58.0` or newer is required for shared build commands. CI and Docker pin Just `1.58.0`.
- CI uses Python `3.13`; Docker uses Python `3.13` and Node `26`. CI consumes committed assets without npm.
- Prefer CI versions when reproducing CI behavior; Docker and development docs may reference older base images.
- Production-like builds may depend on environment variables from `.github/workflows/gh-pages.yml`, including `ATTACK_WEBSITE_GOOGLE_ANALYTICS`, `ATTACK_WEBSITE_GOOGLE_SITE_VERIFICATION`, `ATTACK_WEBSITE_INCLUDE_OSANO`, and `PELICAN_SITEURL`.

## High-Value Commands

Run commands from the repo root unless a subdirectory is called out.

### Install

- All local dependencies: `just install-deps` (creates/reuses root `.venv` and runs `npm ci` in both packages)
- Preferred Python env for manual setup: `uv venv --python 3.13 .venv`
- Python deps: `uv pip install -r requirements.txt`
- Search deps: `cd attack-search && npm ci`
- Style deps: `cd attack-style && npm ci`
- Prefer `npm ci` over `npm install`; do not update lockfiles unless dependency changes are part of the task.

### Build

- Complete website build: `just build-full-website --attack-brand --all-extras`
- Website using staged assets: `just build-website --attack-brand --all-extras`
- Compile and stage assets: `just build-search`, `just build-style`, or `just build-assets`
- Website targets retain Python CLI defaults unless flags are explicitly supplied; builds do not install dependencies.
- Python generator and targeted checks: `uv run python update-attack.py ...`
- Shared build ordering, prerequisites, and Docker integration: `docs/DEVELOPMENT.md`
- Search bundle: `cd attack-search && npm run build`
- Search dev bundle: `cd attack-search && npm run build:dev`
- Copy the compiled search bundle into theme static assets: `cd attack-search && npm run copy`
- Search build + copy into theme static assets: `cd attack-search && npm run build-copy`
- Style build: `cd attack-style && npm run build`
- Style build + copy into theme static assets: `cd attack-style && npm run build-copy`

### Local Validation

- Full local site validation follows `docs/DEVELOPMENT.md` and `test/README.md`.
- Build site output first, then serve `output/` through the Docker test image.
- Test container build: `cd test && docker build -t attack-website-test .`
- Test container run: `cd test && docker run -p 80:80 -v $(pwd)/../output:/workspace attack-website-test`
- Helper script: `cd test && ./run_test.sh`

### Lint And Format

- Python lint (configured, not wired into CI): `ruff check .`
- Python lint autofix: `ruff check --fix .`
- Python format: `ruff format .`
- Search lint: `cd attack-search && npm run lint`
- Search lint autofix: `cd attack-search && npm run lint:fix`
- Style lint: `cd attack-style && npm run lint`

### Tests

- Search tests: `cd attack-search && npm test`
- Single Jest test file: `cd attack-search && npm test -- __tests__/search-service.test.js`
- Alternate single Jest file: `cd attack-search && npx jest __tests__/search-service.test.js`
- Main Python-driven site tests run through the build script, not `pytest`.
- Run specific site test categories: `uv run python update-attack.py -m tests -t size`
- Multiple site test categories: `uv run python update-attack.py -m tests -t links -t external_links -t citations`

### Important Command Notes

- `justfile` defines the shared asset/site build commands. There is no root `package.json`, `Makefile`, or single universal test runner.
- CI builds the site using committed assets without rebuilding or verifying them against source. Docker rebuilds assets. CI does not currently enforce Jest, ESLint, Stylelint, Ruff, or type checks.
- For Python-side testing, the narrowest supported scope is a named category (`size`, `links`, `external_links`, `citations`), not an individual test file.
- Preferred production-like validation is Nginx via Docker, not Pelican's built-in dev server.
- Pelican's built-in development server does not match production Nginx routing behavior.

## Source Of Truth

- Follow existing file-local conventions before applying generic preferences.
- Treat `pyproject.toml`, `attack-search/.eslintrc`, and `attack-style/.stylelintrc.json` as authoritative style configs.
- Treat `docs/DEVELOPMENT.md` and `.github/workflows/gh-pages.yml` as authoritative for build workflow.
- In templates, respect comments that mark generated files or source-of-truth files.
- Example: `attack-theme/templates/general/base-template.html` explicitly says to edit `base-template.html`, not generated `base.html`.

## Generated And Volatile Outputs

- Do not edit `output/` as source; regenerate it through the build pipeline.
- Avoid direct edits to `attack-search/dist/` and `attack-style/dist/` unless the task explicitly targets generated artifacts.
- Avoid direct edits to copied assets in `attack-theme/static/` when a source file in `attack-style/`, `attack-search/` or another generator owns the output.
- Preserve generated-file comments and edit the named source template or source asset instead.
- Ignore intermediate outputs in `attack-search/dist/` and `attack-style/dist/`, but commit the compiled theme CSS and `attack-theme/static/scripts/search_bundle.js` together with frontend source changes. After changing anything in either package, regenerate its assets with `just build-search`, `just build-style`, or `just build-assets`. Keeping them current is the developer's responsibility.
- Keep the build-specific `attack-theme/static/scripts/settings.js` ignored; see `docs/DEVELOPMENT.md` for its runtime configuration role.

## Python Style

- Use 4-space indentation.
- Match Ruff formatting and the configured 120-character line length.
- Keep imports grouped as standard library, third-party, then local imports.
- Use Ruff when reorganizing imports.
- Prefer `snake_case` for variables, functions, and module names.
- Reserve `UPPER_CASE` for constants or config-like values.
- Keep modules function-oriented and simple; the codebase uses few classes outside JS.
- Type hints are not a dominant convention here; do not introduce a large typing layer unless the touched area already uses it.
- Python type hints are desired to be added over time.
- Python docstrings should follow NumPy conventions.

## Python Error Handling

- Raise explicit argument validation errors when input is invalid.
- Preserve existing CLI behavior in `update-attack.py`; it is the operational entry point.
- Avoid silent failures in build code unless the surrounding module already degrades intentionally.
- When editing build logic, prefer predictable failures with useful messages over hidden fallbacks.

## JavaScript Style

- In `attack-search/`, use CommonJS (`require`, `module.exports`) unless the file already uses something else.
- Keep local imports consistent with surrounding code; many files include `.js` extensions intentionally for webpack resolution.
- Prefer single quotes in `attack-search/` unless the local file already differs.
- Semicolons are the norm in `attack-search/`; keep them.
- Use `camelCase` for variables and functions, `PascalCase` for classes.
- Modern JS features are acceptable in `attack-search/` (async/await, private methods, optional chaining, nullish coalescing).
- Favor small, explicit DOM interactions over framework-style abstractions; this repo is not React-based.
- In legacy `attack-theme/static/scripts/`, preserve the file's existing style rather than forcing `attack-search/` conventions into older code.
- Preserve browser compatibility assumptions in legacy theme scripts; avoid modernizing syntax there unless the build path transpiles it.

## JavaScript Error Handling And Testing

- For async startup flows, follow the existing `try/catch` and `.catch()` patterns.
- Log actionable errors with `console.error` or `console.debug` where the surrounding code already does so.
- Prefer graceful UI degradation for browser capability issues instead of crashing the page.
- Jest tests live in `attack-search/__tests__/` and usually use `describe`, `test` or `it`, mocked globals, and fixture files.
- When adding tests, follow the existing jsdom/jQuery mocking style rather than introducing a new browser test stack.

## Templates, HTML, And Content Generation

- Jinja templates typically place `set` statements and imports at the top.
- Preserve existing macro usage patterns instead of inlining repeated HTML.
- Do not edit generated artifacts if the template comments point to a source template.
- Keep ATT&CK branding, banner, and version placeholders intact unless the task is explicitly about site configuration.
- Be careful with path handling and generated `index.html` semantics; many helpers normalize trailing slashes.

## SCSS And Styling

- `attack-style/` uses Sass modules with `@use`, not legacy `@import`.
- Preserve the layered structure: `abstracts/`, `base/`, `layout/`, `components/`.
- Import order matters because variables/functions are dependencies for later files.
- Use lowercase, hyphenated naming for classes and partial filenames.
- Reuse existing Sass variables, maps, and helper functions instead of hardcoding colors or spacing.
- Lint with Stylelint when editing SCSS.

## Naming And File Hygiene

- Keep filenames and identifiers consistent with the surrounding subsystem.
- Prefer focused changes over opportunistic refactors.
- Avoid renaming public paths, generated content paths, or ATT&CK URL structures unless required.
- Preserve comments that explain generation behavior, browser compatibility, or build caveats.

## Do Not

- Do not treat generated output as canonical source.
- Do not change ATT&CK URL structures, permalink behavior, or `index.html` generation casually.
- Do not convert `attack-search/` from CommonJS to ESM unless the task explicitly requires it.
- Do not add frontend frameworks for small browser interactions.
- Do not assume Pelican's development server is sufficient for routing-sensitive validation.

## Agent Workflow Expectations

- Before editing, identify which subsystem you are in: root Python build, `attack-search/`, `attack-style/`, `attack-theme/`, or `modules/`.
- Run the narrowest relevant validation for the files you touched.
- If you changed `attack-search/`, run relevant Jest tests and/or `cd attack-search && npm run lint`.
- If you changed SCSS, run `cd attack-style && npm run lint` and usually `cd attack-style && npm run build`.
- If you changed root build or content-generation code, run at least the relevant `update-attack.py` build or targeted test category.
- If your change affects rendered output or routing, validate with the Docker Nginx test environment when practical.
- For template, routing, or generated-output behavior changes, run the site build and prefer Docker/Nginx validation when practical.

## Git And Contribution Notes

- Pull requests should target the `develop` branch per `docs/CONTRIBUTING.md`.
- The PR template expects a reviewer and a `CHANGELOG.md` update when appropriate.
- The website version is configured in `modules/site_config.py`; keep it aligned with release tags and docs.
- Do not assume `master` is the integration branch just because GitHub Pages deploys from it.
- Use Conventional Commit style git messages.

## When Unsure

- Read the nearest config file and a nearby edited file before making stylistic changes.
- Prefer matching existing conventions over introducing new tools or patterns.
- Keep builds reproducible, paths stable, and generated output compatible with the current pipeline.
