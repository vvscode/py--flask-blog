# Блог

Базовое веб-приложение "Блог".

Для запуска миграций изпользуйте

```
flask db upgrade
```

Для запуска в режиме разработки используйте

```
FLASK_APP=main.py FLASK_ENV=development flask run
```

При работе на Heroku используется gunicorn