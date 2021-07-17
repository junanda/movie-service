from fastapi import FastAPI
from app.api.movie import movies
from app.api.db import metadata, db, db_engine

metadata.create_all(db_engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()

app.include_router(movies)
