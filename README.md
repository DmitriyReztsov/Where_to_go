# Where_to_go Devman study project
Where to go
web: http://dmitriyreztsov.pythonanywhere.com/

# Where_to_go

Бэкенд сайта с POI (point of interest) - интересными местами. Учебный проект в рамках курса Devman. Реализованы создание карточек мест с возможностью привязки географической точки, добавления и ручной сортировки фотографий, редактирования и форматирования описания места.


## Tech

- Python
- Django
- django-admin-sortable2
- django-tinymce


## Installation

Для разворачивания сайта локально склонируйте репозиторий и выполните следующие команды (убедитесь, что выполняете команды под правами рута) для установки зависимостей:
```sh
apt-get install gdal-bin
apt-get install libsqlite3-mod-spatialite
pip install -r requirements.txt
```

Из папки проекта ./where_to_go выполните команды:
```sh
python manage.py migrate --noinput
python manage.py createsuperuser
python manage.py collectstatic --no-input
```

Создайте из файла env_example.txt файла с настройками .env и запустите сервер:
```sh
python manage.py runserver
```


## Author

Dmitriy Reztsov
