from fastapi import FastAPI
from routers import search, getlyrics

# creating instance of the fast api
app = FastAPI()

app.include_router(search.router)
app.include_router(getlyrics.router)
