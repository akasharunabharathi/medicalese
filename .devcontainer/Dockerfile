# Use an official Ubuntu base image
FROM ubuntu:latest

# Set non-interactive installation to avoid getting stuck on configuration prompts
ENV DEBIAN_FRONTEND=noninteractive

# Update the package list and install Python and essential tools
RUN apt-get update && \
    apt install -y git && \
    apt-get install -y python3 python3-pip python3-venv

# Install Tesseract-OCR and its English language package
RUN apt-get install -y tesseract-ocr tesseract-ocr-eng

# Create a virtual environment
RUN python3 -m venv /opt/venv

# Activate the virtual environment
ENV PATH="/opt/venv/bin:$PATH"

# Copy the requirements file from the local `lib` directory to the container
COPY ./lib/requirements.txt /tmp/requirements.txt

# Install Python libraries from requirements.txt
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

# Set the working directory for container to /app
WORKDIR /app

# Copying the application code
COPY ../ /app

# Set the default command to run your application
CMD ["python3", "lib/main.py"]

# Expose the port the app runs on
EXPOSE 80