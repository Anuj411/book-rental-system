FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /documents/projects/book-rental-system/

COPY . .

RUN apt-get update && apt-get install -y sudo
RUN pip install --no-cache-dir virtualenv

RUN virtualenv /venv

RUN sudo /venv/bin/pip install --no-cache-dir -r requirements/production.txt

ENV PATH="/venv/bin:$PATH"

RUN python manage.py seed
RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "book_rental.wsgi:application", "--bind", "0.0.0.0:8000"]
