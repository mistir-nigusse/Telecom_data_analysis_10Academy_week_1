# Use an official Python runtime as a parent image
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Set environment variables
ENV PYTHONUNBUFFERED 1
EXPOSE 6000

# Command to run the application
CMD [ "python", "src/loader.py" ]
