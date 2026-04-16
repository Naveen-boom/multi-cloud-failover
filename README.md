# multi-cloud-failover
AI-based Multi-Cloud Failover System that monitors AWS and GCP servers and automatically switches traffic during failures.

##  Overview
This project is a Multi-Cloud Failover System that ensures high availability of applications by monitoring multiple cloud servers (AWS and GCP) and automatically switching traffic when a failure or high latency is detected.

## Objective
To build a reliable system that minimizes downtime by using intelligent monitoring and automatic failover between cloud providers.

## Features
- Real-time server health monitoring
- Latency-based performance analysis
- Automatic failover between AWS and GCP
- REST API for system status
- Scalable backend using Flask

## Tech Stack
- Python
- Flask
- AWS EC2 (planned)
- Google Cloud Platform (planned)
- HTML/CSS/JS (for dashboard)

## How It Works
1. The system continuously checks the health of cloud servers.
2. If a server fails or becomes slow, the system detects it.
3. Traffic is automatically redirected to the healthy server.
4. The active server status is updated via API.

##  API Endpoints
- `/` → System status message
- `/status` → Returns server health and active cloud

##  Project Status
Day 1 completed – Basic Flask backend setup.

##  Author
Naveen HT
