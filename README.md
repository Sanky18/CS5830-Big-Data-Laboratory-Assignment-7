# FastAPI Monitoring with Prometheus and Grafana

This repository enhances a FastAPI application by adding Prometheus for API monitoring and Grafana for visualization. It also includes dockerization and scaling to multiple instances for comprehensive cluster health monitoring.

## Overview

This project extends a FastAPI application with Prometheus monitoring hooks to track API usage and monitor the application's health. It uses Grafana for visualizing the Prometheus metrics. After verifying the single instance of the application, the project is dockerized and scaled to multiple instances to monitor the health of the cluster.

## Features

- **Prometheus Monitoring**: Track API usage and monitor health metrics.
- **Grafana Visualization**: Visualize Prometheus metrics for insights into API performance.
- **Dockerization**: Seamlessly build and run the application in Docker containers.
- **Scaling**: Deploy multiple instances of the FastAPI application to form a cluster.
- **Metrics**: Monitor API usage counters, runtime, memory utilization, CPU utilization, and network I/O.

## Folder Structure
    ├── Experiments
    ├── Result
    │   ├── dashboard_image_1.png
    │   ├── dashboard_image_2.png
    │   └── ...
    ├── app
    │   ├── Dockerfile
    │   ├── digit_predictor.py
    │   ├── docker-compose.yml
    │   ├── image_formatter.py
    │   ├── main.py
    │   ├── mnist_model.h5
    │   ├── model_loader.py
    │   ├── prometheus.yml
    │   ├── requirements.txt
    │   └── testing.py
    ├── models
    ├── scripts
    │   └── train_best_model.py
    └── tests

## Setup
1. **Clone the repository:**
   ```bash
   git clone <repository-url>
2. **Install dependencies:**
   ```bash
   cd app
   pip install -r requirements.txt
3. Prometheus Configuration
Ensure the prometheus.yml file is in the app directory.

4. Docker Setup
Create a Dockerfile in the app directory to define the dockerization configuration.

5. Docker Compose Configuration
Create a docker-compose.yml file in the app directory to define the services and ports.

6. Build and Run the Docker Containers
Build the Docker image and start the containers.
   ```bash
      docker-compose up --build
7. Access Prometheus and Grafana

- **Prometheus**: Access at [http://localhost:9090](http://localhost:9090)
- **Grafana**: Access at [http://localhost:3001](http://localhost:3001)

8. Setup Grafana Dashboard

Use Grafana to create a dashboard and visualize the metrics from Prometheus. Refer to the images in the Result folder for examples of dashboard configurations.


