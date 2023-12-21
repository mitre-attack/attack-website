# Developer Guide

The sections below explains how to build and run the website locally using Docker & Nginx. If you want to extend the style, content or functionality of this site, please see our [Customizing the ATT&CK Website](/CUSTOMIZING.md) document for tips and tricks.

* Use **Workflow 1** if you need a comprehensive solution that handles both building and serving the website
* Use **Workflow 2** if you're developing and need to quickly test changes without the overhead of the full Docker build process

Use our [Github Issue Tracker](https://github.com/mitre-attack/attack-website/issues) to let us know of any bugs or other issues you encounter. We also encourage pull requests if you've extended the site in a cool way and want to share back to the community!

If you find errors or typos in the site content, please let us know by sending an email to <attack@mitre.org> with the subject **Website Content Error**, and make sure to include both a description of the error and the URL at which it can be found.

_See [CONTRIBUTING.md](/CONTRIBUTING.md) for more information on making contributions to the ATT&CK website._

## Prerequisites

* Docker
* Node.js and npm (for local build)
* Python 3 and pip (for local build)

## Workflow 1: Build and Run Using Docker

This workflow is designed to be a comprehensive, all-in-one solution to building and serving the website. It utilizes a multi-stage Docker build process to handle the entire sequence of operations starting from installing dependencies to generating static files, and ultimately running the website.

The first stage in this Dockerfile leverages a Node.js base image (node:16) to handle JavaScript and Webpack operations required for generating the search bundle of the site.

The second stage uses a Python base image (python:3.10-slim-bullseye) to run the update-attack.py script, which generates static files for the entire website.

The final stage is based on a lightweight Nginx image (nginx:stable-alpine) which is configured to serve the static files generated in the previous stage. In other words, once the Docker image is built, you can run a container from this image and have a fully functional version of the website served by an Nginx server.

This approach is especially suitable if you need to have an isolated and reproducible build process, as each run starts from a clean state and goes through all the steps necessary to produce a running website.

### Steps

1. Build the Docker image:

    ```shell
    docker build -t attack_website .
    ```

2. Run the Docker container:

    ```shell
    docker run -p 80:80 attack_website
    ```

   This will start a Docker container with the image you built and forward port 80 from the container to your host machine.

3. Now, you should be able to view the website by opening a web browser and navigating to `http://localhost`.

## Workflow 2: Build Locally and Serve Using Docker

This workflow, on the other hand, is optimized for developers who need a faster iteration cycle for testing changes to the website. It allows for the website to be built manually on your local system, which can offer more control and faster feedback while making changes to the codebase.

In this workflow, the Dockerfile is much simpler and serves a single purpose: to run an Nginx server that hosts the website. However, instead of embedding the website's static files within the Docker image (as in Workflow 1), these files are provided to the Docker container at runtime through a Docker volume. This volume points to the output/ directory on your local file system, where the build artifacts are located.

The main advantage of this approach is that you can modify the website's source files, run the build process locally, and then refresh your browser to see the changes without having to rebuild the Docker image. This can greatly accelerate the feedback loop when you're making frequent changes to the site.

### Steps

1. Ensure you have Node.js, npm, Python 3, and pip installed on your local machine.

2. Build the static web content locally. The web application is composed of two modules: the Pelican content, and the ATT&CK search module.

    * Build the Pelican content by running the following command from the root of the project:

        ```shell
        python3 update-attack.py --attack-brand --extras --no-test-exitstatus
        ```

      The static web content will be written to a folder called "output".

    * Build the search module by running the following commands:

        ```shell
        cd attack-search
        npm ci
        npm run build
        cp dist/search_bundle.js ../output/theme/scripts/
        cd ..
        ```

3. Build the Docker image for the test environment:

    ```shell
    cd test
    docker build -t attack-website-test .
    ```

4. Run the Docker container for the test environment:

    ```shell
    docker run -p 80:80 -v $(pwd)/../output:/workspace attack-website-test
    ```

   This will start a Docker container with the test environment image, forward port 80 from the container to your host machine, and mount the "output" directory from your local workspace to the "/workspace" directory inside the container. This allows Nginx to serve the static web content you built.

   Please see [test/README.md](./test/README.md) for further usage details on the test environment image.

5. Now, you should be able to view the website by opening a web browser and navigating to `http://localhost`.

Please note that Workflow 1 is the preferred method as it closely emulates our production environment.
Workflow 2 is recommended for those who prefer or need to build the website locally before testing it.

## Disclaimer re: Pelican's Built-in Web Server

We advise that you avoid using Pelican's built-in web server for serving the website.
Pelican uses a different set of rules for path matching compared to Nginx, which is used in our production environment.
As a result, the behavior of the built-in server may differ from the production environment, potentially leading to discrepancies and overlooked issues.

To ensure that your testing environment is as close as possible to the production environment, we recommend using the workflows outlined in this guide.
Both workflows leverage Nginx, which more closely emulate the behavior of the production environment, improving your ability to catch potential issues before they reach production.
