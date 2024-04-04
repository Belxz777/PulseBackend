FROM  python:3.12-alpine

WORKDIR /code
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8000

CMD ["python", "manage.py", "runserver"]  
