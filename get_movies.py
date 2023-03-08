import time
from movies import Movies
from credentials import conn
from sql_queries import create_table, get_movies

create_table(conn)

if __name__ == '__main__':
    while True:
        print(get_movies(conn))
        time.sleep(1)
