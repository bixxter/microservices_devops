import time
from sql_queries import create_table, get_movie_by_id
from credentials import conn

create_table(conn)

if __name__ == '__main__':
    while True:
        print(get_movie_by_id(conn, 1))
        time.sleep(1)