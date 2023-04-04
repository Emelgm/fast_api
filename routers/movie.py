from fastapi import APIRouter
from fastapi import Path, Query, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from schemas.movie import Movie as Mov
from typing import List
from config.database import Session
from middlewares.jwt_bearer import JWTBearer
from services.movie import MovieService

movie_router = APIRouter()

# traer todas las películas
@movie_router.get('/movies', tags=['Movies'], response_model=List[Mov], status_code=200, dependencies=[Depends(JWTBearer())])
def get_movies() -> List[Mov]:
    db = Session() # conexión
    result = MovieService(db).get_movies() 
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

# traer película especificada
@movie_router.get('/movies/{item}/{id}', tags=['Movies'], response_model=Mov)
def get_movie_by_item(item: str, id: int = Path(ge=1, le=1000)) -> Mov:
    db = Session() 
    result = MovieService(db).get_movie_by_id(id)
    if not result:
        return JSONResponse(status_code=404, content={'Message': 'Not found'})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

# movie por categoría
@movie_router.get('/movies/', tags=['Movies'], response_model=List[Mov])
def get_movies_by_category(category: str = Query(min_length=3, max_length=15)) -> List[Mov]:
    db = Session() 
    result = MovieService(db).get_category(category)
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

# crear película
@movie_router.post('/movies', tags=['Movies'], response_model=dict, status_code=201)
def create_movie(movie: Mov) -> dict:
    db = Session() 
    MovieService(db).create_movie(movie)
    return JSONResponse(status_code=201, content={'Message': 'Exitoso'})

# editar película
@movie_router.put('/movies/{id}', tags=['Movies'], response_model=dict)
def update_movie(id: int, movie: Mov) -> dict:
    db = Session()
    result = MovieService(db).get_movie_by_id(id)
    if not result:
        return JSONResponse(status_code=404, content={'Message': 'Not found'})
    MovieService(db).update_movie(id, movie)
    return JSONResponse(status_code=201, content={'Message': 'Modificación Exitosa'})

# eliminar película
@movie_router.delete('/movies/{id}', tags=['Movies'], response_model=dict)
def delete_movie(id: int) -> dict:
    db = Session() 
    result = MovieService(db).get_movie_by_id(id)
    if not result:
        return JSONResponse(status_code=404, content={'Message': 'Not found'})
    MovieService(db).delete_movie(id)
    return JSONResponse(status_code=200, content={'Message': 'Eliminación Exitosa'})