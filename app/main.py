from fastapi import FastAPI
from api.movie import movies

app = FastAPI()

app.include_router(movies)
