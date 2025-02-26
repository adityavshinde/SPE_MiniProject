# Use Ubuntu 22.04 instead of latest
FROM ubuntu:22.04

# Install Python 3.10 and pip
RUN apt-get update && \
    apt-get install -y python3.10 python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy dependency file first for better caching
COPY requirements.txt /app/

# Install dependencies
RUN python3.10 -m pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . /app/

# Set execute permission for the script (if needed)
RUN chmod +x /app/calc.py

# Set the default command to run the calculator script
CMD ["python3.10", "/app/calc.py"]

