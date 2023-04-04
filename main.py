from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.user import user_router

app = FastAPI()

# cambiar config
app.title = 'Mi app'
app.version = '0.0.1'

app.add_middleware(ErrorHandler) # añadir middleware
app.include_router(movie_router) # incluir drutas
app.include_router(user_router) # incluir drutas

Base.metadata.create_all(bind=engine)

@app.get('/', tags=['Home'])
def message():
    return HTMLResponse('<h2>Hola Mundo</h2>')