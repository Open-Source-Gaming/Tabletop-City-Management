#!/bin/bash

CONTAINER_NAME="watson-integration-toolkit"

# Stop the existing container
docker stop $CONTAINER_NAME

# Remove the existing container
docker rm $CONTAINER_NAME

# Navigate to the root of the project
cd "$(dirname "$0")/../../" || exit

# Run a new container with the updated image
docker run --name $CONTAINER_NAME -p 8080:8080 watson-integration-toolkit