# Statistics_counter
Микросервис для счетчиков статистики. 
## Development workflow
Создать новое окружение `python -m venv venv`

Активировать созданное окружение `source venv/bin/activate`, деактивировать - выполнить `deactivate`

Для установки всех зависимостей выполнить `pip install -r requirements.txt`

Для запуска выполнить `python manage.py runserver`

Приложение работает на порту 8000

Для перехода на сайт перейти по ссылке http://127.0.0.1:8000/api/event/

Для перехода на swagger перейти по ссылке http://127.0.0.1:8000/swagger/

GET:
Пример Get запроса для получения всех записей: http://127.0.0.1:8000/api/event/
Пример Get запроса для получения всех записей с 2017-12-30 до 2023-12-30: http://127.0.0.1:8000/api/event/?date_after=2017-12-30&date_before=2023-12-30
Последний запрос, но с сортировкой по кликам: http://127.0.0.1:8000/api/event/?date_after=2017-12-30&date_before=2023-12-30&ordering=clicks
Пример сортировки без даты: http://127.0.0.1:8000/api/event/?ordering=cost
Сортировка в обратную сторону: http://127.0.0.1:8000/api/event/?ordering=-cost

POST:
http://127.0.0.1:8000/api/event/ 
KEY: Content-Type 
VALUE: application/json
Body:
{
    "date": "2017-04-11",
    "views": 43,
    "clicks": 13,
    "cost": 44 
}

DELETE:
http://127.0.0.1:8000/api/event/