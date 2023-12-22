# Resume Checker

## Описание
Сервис для оценивания вашего резюме к вакансии. Нужно ввести текст желаемой вакансии и вашего резюме. 
Далее мы определим степень схожести ваших навыков к требованиям в резюме. Помимо этого рассмотрим ваши сильные и слабые стороны.
Предложим советы для изучения и переписывания вашего резюме.

## Технологии
- Django
- Django REST Framework
- Docker

## Локальная установка и запуск

### Предварительные требования
- Python 3.10 или выше
- pip (Python Package Installer)
- Docker (для Docker-сборки)
- Заданный OPENAI_API_KEY
- Скачанные веса cross-encoder: https://drive.google.com/drive/folders/1FewCy8PhZisQtex84kPy07qlvlEhnxnT?usp=sharing


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
`python manage.py migrate`
`python manage.py runserver 0.0.0.0:8000`

### Использование Docker

1. **Сборка Docker образа:**
`docker build -t my-django-app .`

2. **Запуск Docker контейнера:**
`docker run -p 8000:8000 my-django-app`

## Использование

После запуска проекта, приложение будет доступно по адресу `http://localhost:8000`.


## Исследования:
Можно посмотреть здесь:
https://colab.research.google.com/drive/15eDZQ5ueD6xIE7Wmp2U_Ob-GFNiWFtkg?usp=sharing

### Целевые метрики:
Нужно иметь в виду, что датасет не репрезентативен. Но модель со своей ролью справляется - релевантные резюме и вакансии близко к дург другу. Не релевантные - далеко.

- accuracy: 0.99
- f1_score: 0.99
- recall_score: 1
- precision_score: 0.99
