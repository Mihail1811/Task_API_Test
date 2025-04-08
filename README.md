## Установка зависимостей и запуск тестов

```bash
### Клонирование репозитория

git clone https://github.com/ваш-репозиторий.git
cd simbirsoft_sdet_project

### Установка зависимостей

python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

### Собрать и запустить контейнеры

docker-compose up --build -d

### Или через Makefile:
make run

### Обычный запуск тестов

pytest tests/test_api.py

### Параллельный запуск тестов с отчетом Allure

pytest -n 5 --alluredir=allure-results
allure serve allure-results