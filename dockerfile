FROM python:3.10-slim-buster

COPY requirements.txt /

RUN pip install -r requirements.txt

RUN mkdir /app
WORKDIR /app

COPY post_movies.py /app
COPY sql_queries.py /app
COPY movies.py /app
COPY for_container.py /app

CMD ["python", "/app/for_container.py"]
