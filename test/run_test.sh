#!/bin/bash
docker build -t attack-website-test .
docker run -p 80:80 -v $(pwd)/../output:/workspace attack-website-test
