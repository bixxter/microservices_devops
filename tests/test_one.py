from sqlalchemy import create_engine
from movies import Movies
from sql_queries import insert_movie, get_movies, delete_movie, get_movie_by_id, create_table


def test_insert_movie(postgres_url: str):
    engine = create_engine(postgres_url)
    conn = engine.connect()
    create_table(conn)
    movie = Movies(
        title="The Shawshank Redemption",
        year=1994,
        director="Frank Darabont",
        genre="Drama",
        rating=9.3,
        id=1
    )
    insert_movie(conn, movie)
    assert get_movies(conn) == [movie]
    engine.dispose(postgres_url)


def test_delete_movie(postgres_url: str):
    engine = create_engine(postgres_url)
    conn = engine.connect()

    create_table(conn)
    movie = Movies(
        title="The Shawshank Redemption",
        year=1994,
        director="Frank Darabont",
        genre="Drama",
        rating=9.3,
    )
    insert_movie(conn, movie)
    delete_movie(conn, 1)
    assert get_movies(conn) == []
    engine.dispose(postgres_url)


def test_get_movie_by_id(postgres_url: str):
    engine = create_engine(postgres_url)
    conn = engine.connect()

    create_table(conn)
    movie = Movies(
        title="The Shawshank Redemption",
        year=1994,
        director="Frank Darabont",
        genre="Drama",
        rating=9.3,
        id=1
    )
    insert_movie(conn, movie)
    assert get_movie_by_id(conn, 1) == [movie]

    engine.dispose(postgres_url)