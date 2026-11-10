FROM python:3.12-slim

WORKDIR /app

COPY app.py .

RUN pip install --no-cache-dir pandas

CMD ["python", "app.py"]
