# Use multi-stage build
FROM node:16 as node-build

WORKDIR /app

# Copy package.json, package-lock.json, and webpack configuration
COPY attack-search/package*.json ./attack-search/
COPY attack-search/webpack.config.cjs ./attack-search/

# Copy src/ folder with all subdirectories
COPY attack-search/src ./attack-search/src

# Generate the webpack bundle containing the search service
RUN cd attack-search && \
    npm ci && \
    npm run build

# Use the official Python image as the base image
FROM python:3.10-slim-bullseye as python-build

ENV DEBIAN_FRONTEND noninteractive
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

# Install dependencies
RUN apt-get update --fix-missing && \
    apt-get upgrade -y && \
    apt-get install -y -qq --no-install-recommends locales sudo git apt-transport-https ca-certificates && \
    echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen && \
    update-ca-certificates

WORKDIR /home/attackuser/attack-website

# Copy the source code
COPY . .

# Install all Python dependencies
RUN python3 -m pip install --no-cache-dir wheel && \
    python3 -m pip install --no-cache-dir -r requirements.txt

# Build the website
RUN python3 update-attack.py --no-test-exitstatus

# Copy the search service webpack bundle from the node-build stage
COPY --from=node-build /app/attack-search/dist/search_bundle.js output/theme/scripts/search_bundle.js

# Nginx stage
FROM nginx:stable-alpine as production-stage

COPY --from=python-build /home/attackuser/attack-website/output /var/www/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Label metadata
LABEL name="attack-website" \
    description="Dockerfile for the ATT&CK Website" \
    usage="https://github.com/mitre-attack/attack-website/blob/master/README.md#install-and-build" \
    url="https://attack.mitre.org/" \
    vcs-url="https://github.com/mitre-attack/attack-website" \
    vendor="MITRE ATT&CK" \
    maintainer="attack@mitre.org"

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]