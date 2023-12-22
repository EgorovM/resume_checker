# Используйте официальный образ Python как родительский образ
FROM python:3.10-slim

# Установите рабочую директорию в контейнере
WORKDIR /usr/src/app

# Копируйте файл зависимостей в рабочую директорию
COPY requirements.txt ./

# Установите все зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируйте все файлы проекта в контейнер
COPY . .

# Установите переменные среды
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN python manage.py migrate

# Выполните команду для запуска uWSGI
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]