# backend_community_homework

[![CI](https://github.com/yandex-praktikum/hw02_community/actions/workflows/python-app.yml/badge.svg?branch=master)](https://github.com/yandex-praktikum/hw02_community/actions/workflows/python-app.yml)

##### Учебный проект
#### Доработка приложения yatube.
Новое в проекте:
##### Модели (`models.py`):
- Post
- Group
##### Админка (`admin.py`):
- Кастомизация админки для модели Post: отображаемые поля, редактирование group, поиск и фильтрация.
##### View-функции (`views.py`):
- `index()`: передаёт в шаблон `posts/index.html` десять последних объектов модели Post.
- `group_posts()`: передаёт в шаблон `posts/group_list.html` десять последних объектов модели Post, отфильтрованных по полю `group`, и содержимое для тега `<title>`.
##### Адреса (`urls.py`):
- Для приложения Posts установлен namespace=`posts`.
- для главной страницы установлен name=`index`.
- страница с постами из определённой группы доступна по URL вида `group/<slug>/`.
- для страницы с постами группы установлен name=`group_list`.
##### Шаблоны:
- Разбиты на блоки с помощью `include` и `extend`.

#### Запуск проекта в dev-режиме 
- Установите и активируйте виртуальное окружение: ```python -m venv venv```
- Установите зависимости из файла requirements.txt: ``` pip install -r requirements.txt ``` 
- Создайте миграции и мигрируйте их в БД: ```python manage.py makemigrations```, ```python manage.py migrate```
- Запустите сервер, выполнив в папке с файлом manage.py команду: ``` python manage.py runserver ``` 

##### Финальная версия проекта yatube: https://github.com/creamsandwch/hw05_final.
