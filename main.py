from fastapi import FastAPI
from models.Libro import Libro

app = FastAPI()

@app.get("/")
def index():
    return "Welcome to the FastAPI application! que chevere fastapi"

@app.post("/libros")
async def guardar_libros(libro: Libro) -> Libro:
    print(libro)
    print(f"Libro: {libro.titulo} guardado exitosamente")
    return libro

@app.put("/actualizar_libro/{isbn}")
async def actualizar_libro(isbn: int) -> str:
    print(isbn)
    return f"Libro con ISBN {isbn} actualizado con exito"

@app.delete("/eliminar_libro/{isbn}")
def eliminar_libro(isbn: int) -> str:
    print(isbn)
    return f"Libro con ISBN {isbn} eliminado con exito"