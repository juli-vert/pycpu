# pycpu
Small webservice which retrieves the cpuinfo from the container

Requirements:
-
- Docker

Usage: 
-
- docker pull python:3.6.4-slim-jessie
- docker build -t pycpuinfo .
- docker run -p 8080:8080 pycpuinfo &
- curl http://localhost:8080 | jq
