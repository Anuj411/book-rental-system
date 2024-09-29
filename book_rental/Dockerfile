FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY ../requirements/local.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Run database migrations, collect static files
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

# Use Gunicorn to serve the app
CMD ["gunicorn", "book_rental.wsgi:application", "--bind", "0.0.0.0:8000"]
