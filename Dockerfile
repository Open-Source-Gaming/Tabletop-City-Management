# Use the official Python image from the Docker Hub
FROM python:3.11

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Add Poetry to PATH
ENV PATH="/root/.local/bin:$PATH"

# Set the working directory in the container
WORKDIR /code

# Copy the pyproject.toml and poetry.lock files into the container
COPY ./pyproject.toml ./poetry.lock* /code/

# Install the dependencies
RUN poetry install --no-root

# Copy the rest of the working directory contents into the container
COPY . /code

# Command to run the application
CMD ["poetry", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080"]
