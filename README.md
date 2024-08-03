# Тестовое задание backend разработчик
Стек Django\DRF

Даны модели "Категория Блюд" и "Блюдо" для ресторана.

Даны сериализаторы.

В выборку попадают только Блюда у которых `is_publish=True`.

Если в категории нет блюд (или все блюда данной категории имеют `is_publish=False`) - не включаем ее в выборку.

Запрос в БД сделать любым удобным способом:

Django ORM (предпочтительно), Raw SQL, Sqlalchemy…

Написать View который вернет для API `127.0.0.1/api/v1/foods/` JSON

# Установка

1. Клонируйте репозиторий на свой компьютер:
```
git clone git@github.com:SHURSHALO/restaurant_menu.git
```
2. Создайте и активируйте виртуальное окружение в корне:
```
py -3.9 -m venv venv
```
```
source venv/Scripts/activate
```
3. Установите зависимости:
```
pip install -r requirements.txt
```
4. Создайте `.env` по примеру `.env.example`
5. Примените миграции:
```
cd backend
```
```
python manage.py makemigrations menu
```
```
python manage.py migrate
```
6. Создайте суперпользователя:
```
python manage.py createsuperuser
```
# Запуск

Запустите сервер разработки:
```
python manage.py runserver
```
Заполните БД
Админка по адресу: http://127.0.0.1:8000/admin/
Задание доступно по адресу: http://127.0.0.1:8000/api/v1/foods/
