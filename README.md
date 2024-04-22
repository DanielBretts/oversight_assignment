# Running Oversight Assignment Project with Docker

This guide explains how to pull the Docker image for the Oversight Assignment project and run a Docker container to access the project on port 8000.

## Prerequisites

Before running the project using Docker, ensure you have Docker installed on your system. You can download and install Docker from [here](https://www.docker.com/get-started).

## Pulling the Docker Image

To pull the Docker image for the Oversight Assignment project, execute the following command in your terminal:

```bash
docker pull danielbretts/oversight_assignment:1.00.00
```
Running the Docker Container

Once you have pulled the Docker image, you can run a Docker container using the following command:

```bash
docker run -d -p 8000:8000 danielbretts/oversight_assignment:1.00.00
```

This command will start a Docker container in detached mode (-d), mapping port 8000 of your host machine to port 8000 of the container (-p 8000:8000).

After running the Docker container, you can access the Oversight Assignment project by opening a web browser and navigating to the following URL:

```bash
http://<your_host_ip>:8000
```

## Stopping the Docker Container (Optional)

If you want to stop the Docker container, you can use the following command:

```bash
docker stop <container_id>
```
Replace <container_id> with the ID of the running container. You can find the container ID by running docker ps.
