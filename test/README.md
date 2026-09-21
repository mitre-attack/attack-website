# Test Environment

This directory contains a Docker-based testing environment for the ATT&CK website.
The purpose of this environment is to closely emulate the production GitHub Pages environment, using Nginx to serve the static web content.
This allows developers to catch and fix issues before pushing to GitHub Pages, thereby increasing development efficiency and reducing potential errors in the production environment.

## Prerequisites

Ensure you have the following installed on your local system:

- Docker
- [Just](https://just.systems/man/en/installation.html) 1.58.0 or newer
- [uv](https://docs.astral.sh/uv/getting-started/installation/) and Python 3.13
- Node.js 26 and npm

## Building the Web Application

Before starting the Docker container, install dependencies and build from the
repository root. Just is required for these local build commands:

```shell
just install-deps
just build-full-website --attack-brand --all-extras
```

Installation creates or reuses the root `.venv` and installs both npm packages.
The build compiles and stages Search and Style, then generates the site in `output/`.
For content-only changes, run `just build-website --attack-brand --all-extras`.
The website targets use the Python generator's defaults unless you explicitly pass
options. See the [developer guide](../docs/DEVELOPMENT.md) for setup and build options.

After changing anything in `attack-style/` or `attack-search/`, rebuild the affected
assets and commit the generated files in `attack-theme/static/` alongside your changes.

## Using the Docker Test Environment

1. From the `/test` directory, build the Docker image:

    ```shell
    docker build -t attack-website-test .
    ```

2. Run the Docker container:

    ```shell
    docker run -p 80:80 -v $(pwd)/../output:/workspace attack-website-test
    ```

    This will start a Docker container with the image you built, forward port 80 from the container to your host machine, and mount the "output" directory from your local workspace to the "/workspace" directory inside the container. This allows Nginx to serve the static web content you built.

3. Now, you should be able to view the website by opening a web browser and navigating to `http://localhost`.

To stop the Docker container, press `Ctrl+C` in the terminal where the container is running.

## Helper Script

Alternatively, you can use the `run_test.sh` script to build the Docker image and start the container. Simply run the script from the `/test` directory:

```shell
./run_test.sh
```

Ensure that the script has execute permissions. If needed, you can add execute permissions with the following command:

```shell
chmod +x run_test.sh
```
