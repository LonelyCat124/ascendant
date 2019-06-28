FROM python:3.7-alpine

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "3", "app:app"]