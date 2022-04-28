# Meet up project

### Для запуска

Установка зависимостей
```
pip install -r requirements.txt
```

Создание виртуального окружения (пример можно посмотреть в файле .env.example)
```
echo > .env 'SECRET_KEY="your-secret-key"\nDEBUG=True' 
```

Создание и обновление базы данных
```
python manage.py migrate
```

Запуск сервера
```
python manage.py runserver
```
