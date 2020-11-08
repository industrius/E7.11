Это веб-приложение, построенное на Django DRF, Mongo и Redis. 

Оно является бекендом для доски объявлений. Данные хрнятся в базе данных MongoDB, кеширование проиводится с помощью Redis. 

Чтобы старотовать приложение вам необходимо: 
- склонироавть этот репозиторий 
- перейти в папку с кодом 
- с помощью команды ` docker-compose up -d` запустить приложение. 

Если все успешно,запустятся три контейнера. 

Бекенд приложения стартует на 8008 порту. 

В данном приложении доступны следующие эндпоинты: 
- POST http://<адрес сервера>:8008 добавление новго объявления;
- GET http://<адрес сервера>:8008/<message_id> получение одного сообщения с тегами и комментариями по id;
- POST http://<адрес сервера>:8008/tag добавление тэга к объявлению;
- POST http://<адрес сервера>:8008/comment добавление коментария к объявлению;
- GET http://<адрес сервера>:8008/stat/<message_id> получение статистики по сообщению.

Бонус:
- GET http://<адрес сервера>:8008 получение всего списка объявлений с тэгами и коментами: