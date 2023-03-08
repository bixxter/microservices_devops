import time
import random
from movies import Movies
from credentials import conn
from sql_queries import create_table, insert_movie

create_table(conn)

movies_names = [
    "The Shawshank Redemption",
    "The Godfather",
    "The Godfather: Part II",
    "The Dark Knight"
]

if __name__ == '__main__':
    while True:
        insert_movie(
            conn,
            Movies(
                title=random.choice(movies_names),
                year=random.randint(1990, 2021),
                director=random.choice(["Christopher Nolan", "Quentin Tarantino", "Martin Scorsese"]),
                genre=random.choice(["Action", "Drama", "Comedy"]),
                rating=random.randint(1, 10)
        ))
        print("Created a lot of movies")
        time.sleep(1)
