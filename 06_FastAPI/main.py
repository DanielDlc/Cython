from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def index():
    return {"Hello": "FastAPI"}


@app.get('/produtos/{id}')
async def buscar_produto(id: int):
    return {"id": id}