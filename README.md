Для запуска проекта необходимо:

1.Python 3.11+

2.Postgres SQL (не важна версия)

3.Docker


Команды для ручного запуска приложения:


1.pip install -r requirements.txt (при первом запуске для установки зависимостей)


2.Python manage.py makemigrations  essential (для создания миграции)


3.Python manage.py migrate essential (для применения миграции)


4.Python manage.py runserver (для запуска сервера)


Также возможен запуск через докер:
//собрать image 
//docker run <imageid>
//и все кайфуем 

В ручную:

docker-compose up  --build


Через bat file:

1.Просто запустите run.bat файл для запуска проекта(для запуска необходимо иметь psql, python и docker,версии не так важны , возможны ошибки в отдельных случаях )

2. Порт на котором запускается успешно проебан.



 Используемые инструменты/Tools:
 

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray) ![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens) 




Для просмотра документации эндпоинтов общаться по роуту которого блять не существует , зато есть media какая то залуп которая даже не используется:

/docs


По всем вопросам и предложениям обращаться:

@telegram:belxz999
