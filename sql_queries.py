from sqlalchemy.engine import Connection
from sqlalchemy import text
from movies import Movies

def create_table(conn: Connection):
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS movies (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            year INTEGER NOT NULL,
            director VARCHAR(255) NOT NULL,
            genre VARCHAR(255) NOT NULL,
            rating FLOAT NOT NULL
        )
    """))
    conn.commit()
    

def insert_movie(conn: Connection, movie: Movies):
    conn.execute(text("""
        INSERT INTO movies (title, year, director, genre, rating) VALUES (:title, :year, :director, :genre, :rating)
    """), {
        "title": movie.title,
        "year": movie.year,
        "director": movie.director,
        "genre": movie.genre,
        "rating": movie.rating
    })
    conn.commit()

def get_movies(conn: Connection):
    result = conn.execute(text("""
        SELECT * FROM movies
    """))

    return [
        Movies(
            id=movie[0],
            title=movie[1],
            year=movie[2],
            director=movie[3],
            genre=movie[4],
            rating=movie[5]
        )
        for movie in result
    ]


def get_movies_by_genre(conn: Connection, genre: str):
    result = conn.execute(text("""
        SELECT * FROM movies WHERE genre = :genre
    """), {
        "genre": genre,
    })

    return [Movies(**row) for row in result]

def get_movie_by_id(conn: Connection, id: int):
    result = conn.execute(text("""
        SELECT * FROM movies WHERE id = :id
    """), {
        "id": id,
    })

    return [
        Movies(
            id=movie[0],
            title=movie[1],
            year=movie[2],
            director=movie[3],
            genre=movie[4],
            rating=movie[5]
        )
        for movie in result
    ]


def delete_movie(conn: Connection, id: int):
    conn.execute(text("""
        DELETE FROM movies WHERE id = :id
    """), {
        "id": id,
    })
    conn.commit()

def update_movie(conn: Connection, movie: Movies):
    conn.execute(text("""
        UPDATE movies SET title = :title, year = :year, director = :director, genre = :genre, rating = :rating WHERE id = :id
    """), {
        "title": movie.title,
        "year": movie.year,
        "director": movie.director,
        "genre": movie.genre,
        "rating": movie.rating,
        "id": movie.id
    })
    conn.commit()
