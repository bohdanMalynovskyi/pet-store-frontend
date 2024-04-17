FROM python:3.12.1-alpine

# Устанавливаем зависимости
RUN apk update && apk add libffi-dev gcc musl-dev libressl-dev

# Создаем и активируем виртуальное окружение
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Копируем файл зависимостей и устанавливаем их
COPY requirements.txt /app/
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r /app/requirements.txt

# Копируем приложение в образ
COPY . /app/backend
WORKDIR /app/backend

# Применяем миграции и создаем суперпользователя
CMD ["sh", "-c", "python manage.py migrate && python manage.py createsuperuser --email=admin@example.com --first_name=Олег --second_name=Віталійович --last_name=Петренко --phone_number=0978918623 --noinput && python manage.py runserver 0.0.0.0:8000 --noreload"]


