# Test_Internet_Store
Тестовое задание магазина продуктов для "Сарафана"(Django, DRF, JWT)

# Первое задание

Написать программу, 
которая выводит n первых элементов последовательности 
122333444455555… (число повторяется столько раз, чему оно равно). 

Находится по пути ```./first_task/first_task.py```


# Второе задание

## Установка

1. Скачайте проект в домашнюю директорию.
2. Активируйте виртуальное окружение командой: poetry shell.
3. Установите зависимости командой: poetry install.

## Перед первым запуском программы:

Создайте Базу данных (в данной работе используется PostgreSQL) и перейдите в файл .env.sample и пропишите переменные
окружения в формате(все данные после "=" в виде примера):

```ini
SECRET_KEY = 'django-secret-key'
DEBUG = True/False

DB_NAME = 'name_of_db'
DB_USER = 'db_user'
DB_PASSWORD = 'your_password'
DB_HOST = 'db'
DB_PORT = 5432
```

***

## Работа кода

Выполните команду ```python manage.py runserver```

## Для завершения работы

В терминале выполните команду ```Ctrl+C / Ctrl+Z```








