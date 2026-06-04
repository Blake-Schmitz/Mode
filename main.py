from fastapi import FastAPI
from pydantic import BaseModel
import mode
import uvicorn


URL = '127.0.0.1'
PORT = 6000

app = FastAPI()

class ModeRequest(BaseModel):
    data: list


@app.post('/mode/')
def maximum(request: ModeRequest):
    result = mode.mode(request.data)
    return {'result': result['value'], 'frequency': result['frequency']}

@app.post('/frequency/')
def frequency(request: ModeRequest):
    result = mode.frequency(request.data)
    return result


if __name__ == '__main__':
    uvicorn.run(app, host = URL, port = PORT)