# Приложение для оплаты товаров через stripeAPI
 Сервер со страницей информации о товаре и простой формой оплаты через stripeAPI
## Установка
1. Скопировать репозиторий <br>
```
git clone https://github.com/Dimalright/payment.git 
```
2. Установить зависимости из файла requirements.py
```
```
3. Добавить `.env` фаил указав свои параметры, <br>
   а так же добавить публичный ключ stripe в файле settings.py основной директории
```
```
4. Установить [docker-compose](https://docs.docker.com/compose/install/#install-compose)
## Запуск
Для запуска сайта выполните команду
```
Для корректной работы лучше запускать контейнеры поочередно:
 1)Запускаем базу данных - docker-compose up -d db
 2)Запускаем проект - docker-compose up -d django
В запущенном контенере django выполняем:
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input 
```

## Примеры запросов:
```
https://dimalright.pythonanywhere.com/item/1
```
```
https://dimalright.pythonanywhere.com/buy/1
_______
```
Проект развернут на https://dimalright.pythonanywhere.com/
```

