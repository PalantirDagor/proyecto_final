from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return "Welcome to the FastAPI application! que chevere fastapi"

@app.post("/libros")
async def guardar_libros(dict: dict = {}) -> dict:
    print(dict)
    return "libro guardado con exito"
