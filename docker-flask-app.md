
# Dockerized Flask App - Step-by-Step Deployment

## Objective
Package and deploy a simple Flask app using Docker on AWS EC2 (Ubuntu).

## Files
- app.py - The actual Flask application.
- Dockerfile - Instructions for building the Docker image.

---

## Step 1 - Build Docker Image
```bash
sudo docker build -t flask-app:v1 .

## Step 2- Run Flask COntainer
sudo docker run -d -p 5000:5000 flask-app:v1


## Step 3 - Update Security Group in AWS EC2
	Open port 5000 in the security group to allow external access.

## Step 4 - Check Rnunning containers
sudo docker ps

##Step 5 - Clean
sudo docker stop <container-id>
sudo docker rm <container-id>

