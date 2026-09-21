# Docker build guide

The root `Dockerfile` uses the [Just build commands](DEVELOPMENT.md#commands-and-generator-options) to compile Sass and search before generating the static website, then serves the resulting site with Nginx. It uses Node.js 26 (`node:26-trixie-slim`), Python 3.13 (`python:3.13-slim-trixie`), and `nginx:stable-alpine`.

The `assets-build` stage runs `just build-assets`; the Python stage runs
`just build-website`. Both stages use Just's official
[pre-built binary installer](https://just.systems/man/en/pre-built-binaries.html)
with `--tag 1.58.0 --to /usr/local/bin` and verify the installed version.
The installer selects the binary for the build stage's architecture.
Docker rebuilds assets from source, while GitHub Pages uses committed assets.
Just is installed inside the build images and is not required on the host for this
Docker-only workflow. The final Nginx image does not include Just.

## Build and run

Build the production image from the repository root:

```shell
docker build -t attack-website .
docker run --rm -p 80:80 attack-website
```

The website is then available at <http://localhost>.

## Build arguments

Use `--build-arg NAME=value` to customize a build. All project-owned build arguments use the `ATTACK_WEBSITE_` prefix; `PELICAN_*` arguments are passed directly to Pelican and remain unchanged. `ATTACK_WEBSITE_ATTACK_BRAND`, `ATTACK_WEBSITE_BANNER_ENABLED`, `ATTACK_WEBSITE_INCLUDE_OSANO`, `ATTACK_WEBSITE_TEST_EXITSTATUS`, and `ATTACK_WEBSITE_UPDATE_ATTACK_ALL_EXTRAS` are passed to Typer and accept its Boolean values: `1`, `true`, `t`, `yes`, `y`, and `on` enable a setting; `0`, `false`, `f`, `no`, `n`, and `off` disable it. The Docker-only `ATTACK_WEBSITE_GENERATE_STIX_CHANGELOG` argument requires the exact lowercase value `true` to enable it; every other value disables it.

| Argument | Default | Purpose |
| --- | --- | --- |
| `ATTACK_WEBSITE_ATTACK_BRAND` | `false` | Use the ATT&CK-branded theme. |
| `ATTACK_WEBSITE_BANNER_ENABLED` | CLI default (`true`) | Show the site banner. |
| `ATTACK_WEBSITE_BANNER_MESSAGE` | Custom-instance message | Set the banner content. |
| `ATTACK_WEBSITE_INCLUDE_OSANO` | `false` | Include the Osano privacy script. |
| `ATTACK_WEBSITE_TEST_EXITSTATUS` | `true` | Preserve a nonzero exit status when site tests fail. |
| `ATTACK_WEBSITE_UPDATE_ATTACK_ALL_EXTRAS` | `false` | Run every optional extra module. |
| `ATTACK_WEBSITE_UPDATE_ATTACK_EXTRAS` | Empty | Space-separated optional extra modules, such as `resources blog`. |
| `ATTACK_WEBSITE_STIX_LOCATION_ENTERPRISE` | MITRE CTI Enterprise bundle | Override the Enterprise STIX source. |
| `ATTACK_WEBSITE_STIX_LOCATION_MOBILE` | MITRE CTI Mobile bundle | Override the Mobile STIX source. |
| `ATTACK_WEBSITE_STIX_LOCATION_ICS` | MITRE CTI ICS bundle | Override the ICS STIX source. |
| `ATTACK_WEBSITE_STIX_LOCATION_PRE` | MITRE CTI PRE bundle | Override the PRE-ATT&CK STIX source. |
| `PELICAN_SITEURL` | Empty | Set Pelican's canonical site URL. |
| `ATTACK_WEBSITE_GOOGLE_ANALYTICS` | Empty | Set the Google Analytics identifier. |
| `ATTACK_WEBSITE_GOOGLE_SITE_VERIFICATION` | Empty | Set the Google site-verification value. |
| `ATTACK_WEBSITE_GENERATE_STIX_CHANGELOG` | `false` | Generate a STIX changelog in the image. |
| `ATTACK_WEBSITE_VERSION_ARCHIVE_DIR` | `/var/cache/attack-website/version-archives` | Archive cache location. |
| `ATTACK_WEBSITE_ATTACK_RELEASES_DIR` | `/var/cache/attack-website/attack-releases` | Downloaded release cache location. |
| `ATTACK_WEBSITE_DIFF_STIX_VERSION` | `v19.1` | Prior ATT&CK version used for changelog generation. |

`ATTACK_WEBSITE_UPDATE_ATTACK_ALL_EXTRAS` and `ATTACK_WEBSITE_UPDATE_ATTACK_EXTRAS` are mutually exclusive, just like `--all-extras` and `--extras` in `update-attack.py`.

For example, build an ATT&CK-branded image with all optional extras:

```shell
docker build \
  --build-arg ATTACK_WEBSITE_ATTACK_BRAND=true \
  --build-arg ATTACK_WEBSITE_UPDATE_ATTACK_ALL_EXTRAS=true \
  -t attack-website .
```

## Test exit behavior

The Docker build does not add `--no-test-exitstatus`. Instead, it exports `ATTACK_WEBSITE_TEST_EXITSTATUS` to `update-attack.py`, whose Typer option reads that environment variable. The default (`true`) makes the Docker build fail when the site tests fail. To retain the generated site and treat site-test failures as warnings, set it to `false`:

```shell
docker build --build-arg ATTACK_WEBSITE_TEST_EXITSTATUS=false -t attack-website .
```

This setting affects site-test failures only. Other `update-attack.py` failures still stop the Docker build.

## Workbench credentials

Pass the Workbench API key through a BuildKit secret; do not put it in a build argument or image environment variable. Supply `ATTACK_WEBSITE_WORKBENCH_USER` as a build argument when using the secret:

```shell
docker build \
  --build-arg ATTACK_WEBSITE_WORKBENCH_USER=example-user \
  --secret id=workbench_api_key,src=/path/to/workbench-api-key \
  -t attack-website .
```

The Dockerfile also supports `ATTACK_WEBSITE_OS_CA_TRUST_SETUP_COMMAND` and `ATTACK_WEBSITE_PYTHON_CA_TRUST_SETUP_COMMAND` for environments that require additional certificate trust configuration. Both default to the POSIX no-op command (`:`). The OS trust setup runs in both build stages before downloading Just.
