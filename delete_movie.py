import time
from sql_queries import create_table, delete_movie
from credentials import conn

create_table(conn)

if __name__ == '__main__':
    while True:
        print(delete_movie(conn, 1))
        time.sleep(1)
