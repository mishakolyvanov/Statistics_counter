# Statistics_counter
Микросервис для счетчиков статистики. 
## Development workflow
Создать новое окружение `python -m venv venv`

Активировать созданное окружение `source venv/bin/activate`, деактивировать - выполнить `deactivate`

Для установки всех зависимостей выполнить `pip install -r requirements.txt`

Сделать миграцию `python manage.py migrate` 

Для запуска выполнить `python manage.py runserver`

Приложение работает на порту 8000

Для перехода на сайт перейти по ссылке http://127.0.0.1:8000/api/event/

Для перехода на swagger перейти по ссылке http://127.0.0.1:8000/swagger/

GET:<br>
Пример Get запроса для получения всех записей: http://127.0.0.1:8000/api/event/ <br>
Пример Get запроса для получения всех записей с 2017-12-30 до 2023-12-30: http://127.0.0.1:8000/api/event/?date_after=2017-12-30&date_before=2023-12-30 <br>
Последний запрос, но с сортировкой по кликам: http://127.0.0.1:8000/api/event/?date_after=2017-12-30&date_before=2023-12-30&ordering=clicks <br>
Пример сортировки без даты: http://127.0.0.1:8000/api/event/?ordering=cost <br>
Сортировка в обратную сторону: http://127.0.0.1:8000/api/event/?ordering=-cost <br>

POST:<br>
http://127.0.0.1:8000/api/event/ <br>
KEY: Content-Type <br>
VALUE: application/json<br>
Body:<br>
{<br>
    "date": "2017-04-11",<br>
    "views": 43,<br>
    "clicks": 13,<br>
    "cost": 44 <br>
}<br>

DELETE:<br>
http://127.0.0.1:8000/api/event/