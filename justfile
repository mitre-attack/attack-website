set positional-arguments

python := env('PYTHON', if path_exists(justfile_directory() / '.venv/bin/python') == 'true' { justfile_directory() / '.venv/bin/python' } else { 'python3' })

# The generator invokes Pelican through PATH, so use the selected environment's tools too.
python-path := if python =~ '/' { parent_directory(python) + ':' + env('PATH') } else { env('PATH') }

# List available commands.
_default:
    @just --list

# Install npm dependencies and Python requirements in the repository's .venv.
install-deps:
    test -f .venv/pyvenv.cfg || uv venv --python 3.13 .venv
    uv pip install --python .venv/bin/python -r requirements.txt
    npm --prefix attack-search ci
    npm --prefix attack-style ci

# Compile and stage the production search bundle.
build-search:
    npm --prefix attack-search run build-copy

# Compile and stage all three stylesheets.
build-style:
    npm --prefix attack-style run build-copy

# Compile and stage both search and style assets.
build-assets: build-search build-style

# Generate the site; optional arguments go to update-attack.py.
[env('PATH', python-path)]
build-website *args: _check-assets
    {{ quote(python) }} update-attack.py "$@"

# Rebuild search and style assets, then generate the site with optional update-attack.py arguments.
[env('PATH', python-path)]
build-full-website *args: build-assets _check-assets
    {{ quote(python) }} update-attack.py "$@"

_check-assets:
    @for asset in scripts/search_bundle.js style-attack.css style-user.css style-archive.css; do \
        if [ ! -s "attack-theme/static/$asset" ]; then \
            echo "Missing staged asset: attack-theme/static/$asset. Run 'just build-assets' first." >&2; \
            exit 1; \
        fi; \
    done
