# Установка

## На Linux

Скачать репозиторий:

```sh
git clone https://github.com/txx4G/traffic
```

Заполнить переменные окружения, добавив и заполнив файл `.env`

Собрать образ:

```sh
docker-compose build
```

Запустите контейнер:

```sh
docker-compose up -d
```

## На Windows

### Установка GDAL

1. Выполнить `pip install -r requirements.windows.txt`
3. В `.env` добавить:
    - `GDAL_LIBRARY_PATH=../.venv/Lib/site-packages/osgeo/gdal304.dll`
    - `GEOS_LIBRARY_PATH=../.venv/Lib/site-packages/osgeo/geos_c.dll`

### Установка Spatialite

1. Извлечь все `*.dll` из `mod_spatialite-5.1.0-win-amd64.7z` в `.venv/Scripts`
3. В `.env` добавить: `SPATIALITE_LIBRARY_PATH=mod_spatialite`

### Запуск

Клонируйте репозиторий:

```sh
git clone https://github.com/txx4G/traffic
```

Установите зависимости:

```sh
pip install -r requirements.txt
```

Применените миграции:

```sh
python manage.py migrate
```

Соберите статические файлы:

```sh
python manage.py collectstatic
```


Заполните переменные окружения, добавив и заполнив файл `.env`

Запутите сервер:

```sh
python manage.py runserver 8010
```

## Проверка доступности сервера

<http://127.0.0.1:8020/>

## Примените Nginx + Debian

Настройки для Nginx:

```
server {
    server_name вашдомен.рф www.вашдомен.рф;
    root /usr/share/nginx/html/traffic;
    location / {
        proxy_pass http://127.0.0.1:8020;
    }
    location /static/	 {
        sendfile on;
        root /usr/share/nginx/html/traffic;
    }
    location /media/	 {
        sendfile on;
        root /usr/share/nginx/html/traffic;
    }
    location = /favicon.ico {
        sendfile on;
        root /usr/share/nginx/html/traffic/static;
    }
}
```

Установите сертификат SSL для домена, [согласно инструкциям](https://www.nginx.com/blog/using-free-ssltls-certificates-from-lets-encrypt-with-nginx/) - поправка: возможно, на Вашем сервере нужно вместо команды `python` использовать `python3`.
Если Вы ранее выполнили команды из инструкции, то выполните команду `sudo certbot --nginx -d вашдомен.рф -d www.вашдомен.рф`, чтобы получить сертификат.
