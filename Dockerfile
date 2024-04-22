# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Upgrade pip
RUN pip install --upgrade pip

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

RUN apt-get update

EXPOSE 8000

ENV MAPILLARY_API_KEY <YOUR_MAPILLARY_API_KEY>

CMD ["uvicorn", "server.server:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
