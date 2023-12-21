# Resume Checker

## Описание
Сервис для оценивания вашего резюме к вакансии. Нужно ввести текст желаемой вакансии и вашего резюме. 
Далее мы определим степень схожести ваших навыков к требованиям в резюме. Помимо этого рассмотрим ваши сильные и слабые стороны.
Предложим советы для изучения и переписывания вашего резюме.

## Технологии
- Django
- Django REST Framework
- Docker
- Любые другие технологии, используемые в проекте

## Локальная установка и запуск

### Предварительные требования
- Python 3.8 или выше
- pip (Python Package Installer)
- Docker (для Docker-сборки)
- Заданный OPENAI_API_KEY

### Установка и запуск
Чтобы запустить проект локально, выполните следующие шаги:

1. **Клонирование репозитория:**
```bash
git clone https://github.com/EgorovM/resume_checker.git
cd resume_checker
```
2. **Настройка виртуального окружения (опционально):**
```bash
python -m venv venv
source venv/bin/activate # Для Linux/macOS
venv\Scripts\activate # Для Windows
```

3. **Установка зависимостей:**
`pip install -r requirements.txt`


4. **Запуск проекта:**
`python manage.py runserver`

### Использование Docker

1. **Сборка Docker образа:**
`docker build -t my-django-app .`

2. **Запуск Docker контейнера:**
`docker run -p 8000:8000 my-django-app`

## Использование

После запуска проекта, приложение будет доступно по адресу `http://localhost:8000`.
