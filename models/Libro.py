from pydantic import BaseModel

class Libro(BaseModel):
    autor: str
    titulo: str
    isbn: int
    editorial: str
    anio_edicion: str
    num_paginas: int