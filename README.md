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


## Масштабируемость системы:

При дальнейшем росте количества пользователей, следует вынести три отдельных сервиса:
- Сервис для оценивания и ранжирования вакансий
- Сервис для текстовых описаний улучшений и рефлексии над резюме
- Сервис REST для работы с вакансиями и резюме

Первый сервис можно масштабировать вертикально, так как сложность моделей не менеяется, и так мы можем контролировать количество обрабатываемых запросов
Второй сервис будет являтся ботлнеком системы. В первое время сервис будет использовать открытый API от OpenAI, это ведет к некоторым рискам: повышение цен, неконтролируемость системы и возможный просадкам. Необходимо будет на основе первых 20 тысяч обработанных данных (где то 50$), обучить свою собственную in-house модель. Обучить можно разными способами: SFT маленькой модели, либо PEFT над большими моделями. Первый способ ведет к возможному катастрофическому забыванию, что возможно не лучшее решение. Второе решение видется более приоритетным, так как будет требоваться меньше данных и можно обучить сложную модель с знаниями о мире, например llama-2-70b или openchat. Масштабироваться этот сервис будет так же вертикально.
Третий сервис будет io-сервисом, так как он будет отстветственен за роутинг запросов пользователей. Поэтому можно сделать его ассинхронным, например на основе fastapi. Сервис будет масштабироваться вертикально

## Исследования:
Можно посмотреть здесь:
https://colab.research.google.com/drive/15eDZQ5ueD6xIE7Wmp2U_Ob-GFNiWFtkg?usp=sharing

Подробный репозиторий с оценками:
https://gitlab.com/gopstop/resume_checker_train