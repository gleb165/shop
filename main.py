from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"
@app.get("/name/{name}")
async def root(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {'model_name': 'alexnet', 'message': 'Deep Learning FTW!'}
    if model_name.value == ModelName.resnet:
        return {'model_name': 'resnet', 'message': 'LeCNN all the images'}

    return {'model_name': 'lenet', 'message': 'Have some residuals'}
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}