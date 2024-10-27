#!/bin/bash

# Navigate to your project directory
cd "$(dirname "$0")/../../" || exit

# Deactivate any currently active virtual environment if deactivate command exists
if command -v deactivate &> /dev/null
then
    deactivate
elif command -v conda &> /dev/null
then
    conda deactivate
fi

# Ensure Poetry is installed
if ! command -v poetry &> /dev/null
then
    echo "Poetry is not installed. Please install Poetry first."
    exit 1
else
    poetry --version
fi

# Install dependencies and set up the virtual environment
poetry install

# Verify installation
poetry show --tree

# Activate the virtual environment
poetry shell