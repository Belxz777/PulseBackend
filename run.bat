docker-compose build
docker-compose exec backend python manage.py migrate --noinput
docker-compose up -d
