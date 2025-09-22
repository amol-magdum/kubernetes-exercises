# Dockerfile
FROM python:3.11-slim
ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1
WORKDIR /app
COPY log_writer.py .
RUN pip install flask
CMD ["python", "log_writer.py"]