from sqlalchemy import (Column, Integer, MetaData,
                        String, Table, create_engine, ARRAY, engine)
from database import Database


DATABASE_URL = "sqlite:///./movies.db"

db = Database(DATABASE_URL)

metadata = MetaData()

movies = Table(
    'movies',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('plot', String(50)),
    Column('genres', ARRAY(String)),
    Column('casts', ARRAY(String))
)

db_engine = create_engine(DATABASE_URL, connect_args={
                          "check_same_thread": False})
