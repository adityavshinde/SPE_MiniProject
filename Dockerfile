# Use latest Ubuntu as base image
FROM ubuntu:latest

# Install Python 3.10, pip, and venv
RUN apt-get update && \
    apt-get install -y python3.10 python3-pip python3.10-venv && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy dependency file first for better caching
COPY requirements.txt /app/

# Create a virtual environment
RUN python3.10 -m venv /app/venv

# Activate virtual environment and install dependencies
RUN /app/venv/bin/pip install --upgrade pip && /app/venv/bin/pip install -r requirements.txt

# Copy the rest of the application files
COPY . /app/

# Set execute permission for the script (if needed)
RUN chmod +x /app/calc.py

# Set the virtual environment as default for future commands
ENV PATH="/app/venv/bin:$PATH"

# Set the default command to run the calculator script
CMD ["python3", "/app/calc.py"]
