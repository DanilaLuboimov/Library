# Library
![](https://img.shields.io/badge/Python-3.10-blue?style=flat-square&color=05f) 
![](https://img.shields.io/badge/PostgresSQL-15.1-blue?style=flat-square&color=05f) 
![](https://img.shields.io/badge/Django-4.2.4-blue?style=flat-square&color=004f0d) 
![](https://img.shields.io/badge/psycopg2--binary-2.9.7-9cf?style=flat-square)
![](https://img.shields.io/badge/Django--recaptcha-4.2.4-blue?=flat-square&color=22004f) 
![](https://img.shields.io/badge/Pillow-10.0.0-blue?style=flat-square&color=004f4f) 
![](https://img.shields.io/badge/requests-2.31.0-blue?style=flat-square&color=911010) 
![](https://img.shields.io/badge/JS-clear-blue?style=flat-square&color=e06c28) 
![](https://img.shields.io/badge/Bootstrap-5.3-blue?style=flat-square&color=5c0a8f) 
![](https://img.shields.io/badge/Docker-23.0.5-blue?style=flat-square&color=05f) 
![](https://img.shields.io/badge/Docker--compose-3.8-blue?style=flat-square&color=05f) 

## Реализовано

1. Модели: книги, категории, авторы, кастомные пользователи, обратная связь
2. Заполнение базы (таблицы: книги, категории, авторы) через парсинг файла 
   json по url-адресу
3. Просмотр каталога книг (без фильтров, с фильтрами по категориям, авторам, 
   названиям и публикации) с пагинацией
4. Детальный просмотр каждой книги
5. Регистрация пользователей
6. Авторизация пользователей через модальное окно
7. Форма обратной связи - через модальное окно с автозаполнением, если 
   пользователь авторизован, и с последующим уведомлением на 
   почту
8. Приложение обёрнуто в Docker-compose и использует .env-файл
9. Фронт написан на чистом JS, jQuery и Bootstrap


## Запуск приложения

###### Для работы почты необходимо указать свои переменные в файл .env
~~~
EMAIL_USERNAME=
EMAIL_PASSWORD=
~~~

### Необходимо создать папку "pg_data", в корневой директории проекта, для хранения базы данных

###### Запуск docker-compose

~~~
docker-compose -f ./docker/books_production/docker-compose.yaml --env-file .env up
~~~

Создание миграций и сами миграции применяются командой, описанной 
в docker-compose

###### Для входа в админ панель необходимо добавить superuser
~~~
python manage.py createsuperuser
~~~


### Команда для парсинга данных через терминал
Команда - parse_books_json_by_url <br>
Пример url - https://gitlab.grokhotov.ru/hr/symfony-test-vacancy/-/raw/main/books.json?inline=false
~~~
python manage.py parse_books_json_by_url https://gitlab.grokhotov.ru/hr/symfony-test-vacancy/-/raw/main/books.json?inline=false
~~~

