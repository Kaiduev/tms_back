# Task Management System

### Инструкция по развертыванию проекта на локальную машину

1. Клонирование проекта:
``
git clone https://github.com/Kaiduev/tms_back.git
``
2. Создание виртуального окружения проекта: ``python3 -m venv venv``
3. Активация виртуального окружения: ``source venv/bin/activate``, на платформе виндоус чуть отличается: ``venv\Scripts\activate.bat``
4. Установка зависимостей проекта: ``pip install -r requirements.txt``
5. Запуск миграций: ``python manage.py migrate``
6. Заполнение базы тестовыми данными из файла **test_initial_data.json** выполняется с помощью команды: ``python manage.py loaddata test_initial_data.json``
7. Запуск тестов: ``python manage.py test``
8. Запуск проекта: ``python manage.py runserver``
9. Для работы кэширования убедитесь что в вашей системе установлен Redis и работает под след портом, путь: **redis://127.0.0.1:6379/1**


### Ссылки

1. Апи документация(swagger): http://127.0.0.1:8000/swagger/

### Контакты
1. Telegram username: **@tomasbek**
2. Email: **kaiduevbaktygul07@gmail.com**
