FROM python:3.11.15

WORKDIR /app

COPY . . 

EXPOSE 5000

CMD python server.py