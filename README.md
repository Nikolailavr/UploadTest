# Тестовое задание: Загрузка и обработка файлов

## Цель:
Разработать Django REST API, который позволяет загружать файлы на сервер, а затем асинхронно обрабатывать их с использованием Celery.


## Запуск контейнеров:

```sh
$ docker-compose up -d --build
```

## HELP
http://localhost:8000/upload/ - Принимает POST-запросы для загрузки файлов

http://localhost:8000/files/ - Возращает список всех файлов с их данными, включая статус обработки

Для просмотра задач celery доступен flower на http://localhost:5555