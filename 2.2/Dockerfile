FROM python:3.11-slim
WORKDIR /app
COPY . /app/
RUN pip install -r requirements.txt
# Use /cache as a persistent volume for images
VOLUME /cache
CMD ["python", "pic_server.py"]
