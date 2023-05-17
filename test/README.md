# Test Environment

This directory contains a Docker-based testing environment for the ATT&CK website. The purpose of this environment is to closely emulate the production GitHub Pages environment, using Nginx to serve the static web content. This allows developers to catch and fix issues before pushing to GitHub Pages, thereby increasing development efficiency and reducing potential errors in the production environment.

## Prerequisites

Ensure you have the following installed on your local system:
- Docker
- Node.js and npm
- Python 3 and pip

## Building the Web Application

Before starting the Docker container, you need to build the static web content locally. The web application is composed of two modules: the Pelican content, and the ATT&CK search module.

1. Generate the static web pages (i.e., the Pelican content) by running the following command from the root of the project:

    ```shell
    python3 update-attack.py --attack-brand --extras --no-test-exitstatus
    ```

    The static web content will be written to a folder called "output".

2. Build the search module by running the following commands:

    ```shell
    cd attack-search
    npm ci
    npm run build
    cp dist/search_bundle.js ../output/theme/scripts/
    cd ..
    ```

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
