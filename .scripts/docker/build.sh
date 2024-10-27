#!/bin/bash

# Navigate to the root of the project
cd "$(dirname "$0")/../../" || exit

# Build the Docker image
docker build -t watson-integration-toolkit .
