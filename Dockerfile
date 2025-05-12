FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    gettext \
    vim \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

CMD ["sh", "-c", "for i in {1..30}; do if pg_isready -h db -p 5432 -U $${POSTGRES_USER}; then echo 'PostgreSQL is ready'; break; fi; echo 'Waiting for PostgreSQL to be ready...'; sleep 2; done && python manage.py migrate && gunicorn site_book.wsgi:application --bind 0.0.0.0:8000"]
