FROM python:3.12-slim

WORKDIR /app

COPY app.py .
COPY test_app.py .

RUN pip install psycopg2-binary

CMD ["python", "app.py"]