from pydantic import BaseModel, Field
from typing import Optional

class Movie(BaseModel):
    # validaciones de datos
    id: Optional[int] = None
    title: str = Field(max_length=15)
    overview: str = Field(min_length=10, max_length=50)
    year: int = Field(le=2023)
    rating: float = Field(ge=1, le=10)
    category: str = Field(min_length=3, max_length=15)

    # configuración de prueba
    class Config:
        schema_extra = {
            'example': {
                'id': 20,
                'title': 'Prueba',
                'overview': 'Descripción',
                'year': 2000,
                'rating': 5,
                'category': 'Prueba'
            }
        }