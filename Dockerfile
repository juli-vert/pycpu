FROM python:3.6.4-slim-jessie
RUN pip install flask
WORKDIR /app
COPY os_pycpu.py .
COPY webservice.py .
EXPOSE 8080
ENTRYPOINT ["python", "webservice.py"]
