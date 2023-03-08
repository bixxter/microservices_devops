from typing import Generator
import pytest
from sqlalchemy import Connection, create_engine
from testcontainers.postgres import PostgresContainer

from sql_queries import create_table, insert_movie
from movies import Movies

@pytest.fixture()
def postgres_container1() -> Generator[PostgresContainer, None, None]:
    with PostgresContainer(image="postgres:latest") as container:
        container.start()
        yield container


@pytest.fixture()
def postgres_container() -> PostgresContainer:
    container = PostgresContainer(image="postgres:latest")
    container.start()
    return container


@pytest.fixture()
def postgres_url(postgres_container: PostgresContainer) -> str:
    engine = create_engine(postgres_container.get_connection_url())
    conn = engine.connect()

    create_table(conn)
    return postgres_container.get_connection_url()


@pytest.fixture(scope="function")
def conn_with_data(postgres_container: PostgresContainer) -> str:
    engine = create_engine(postgres_container.get_connection_url())
    conn = engine.connect()

    create_table(conn)
    #     "The Shawshank Redemption",
    # "The Godfather",
    # "The Godfather: Part II",
    # "The Dark Knight"
    movies = [
        Movies(
            title="The Shawshank Redemption",
            year=1994,
            director="Frank Darabont",
            genre="Drama",
            rating=9.3
        ),
        Movies(
            title="The Godfather",
            year=1972,
            director="Francis Ford Coppola",
            genre="Crime",
            rating=9.2
        ),
        Movies(
            title="The Godfather: Part II",
            year=1974,
            director="Francis Ford Coppola",
            genre="Crime",
            rating=9.0
        ),
        Movies(
            title="The Dark Knight",
            year=2008,
            director="Christopher Nolan",
            genre="Action",
            rating=9.0
        )
    ]
    for movie in movies:
        insert_movie(conn, movie)
    return postgres_container.get_connection_url()
