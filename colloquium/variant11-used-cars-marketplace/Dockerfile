FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app

ENV APP_ENV=production
ENV STUDENT_ID=11
ENV SERVICE_NAME=used-cars-marketplace
ENV DEFAULT_CURRENCY=UAH

EXPOSE 8011

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8011"]
