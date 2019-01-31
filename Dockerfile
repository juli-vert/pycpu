FROM python:3.7-alpine
RUN pip3.7 install flask
WORKDIR /app
COPY pycpu.py .
COPY webservice.py .
EXPOSE 8080
CMD ["python3", "webservice.py"]
