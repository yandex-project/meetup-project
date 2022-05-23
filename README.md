# Meet up project

### Для запуска

Установка зависимостей
```
pip install -r requirements.txt
```

Создание виртуального окружения (пример можно посмотреть в файле .env.example)
```
echo > .env 'SECRET_KEY="your-secret-key"\nDJEYM_YMAPS_API_KEY="ymaps_api_key"\nDEBUG=True' 
```
Ключ для DJEYM_YMAPS_API_KEY можно получить здесь: https://developer.tech.yandex.ru/ (JavaScript API Яндекс.Карт)

Создание и обновление базы данных
```
python manage.py migrate
```

Создание карты
```
python manage.py setupmap
```

Запуск сервера
```
python manage.py runserver
```
