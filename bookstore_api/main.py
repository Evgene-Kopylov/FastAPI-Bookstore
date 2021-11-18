from fastapi import FastAPI
# import uvicorn

from config import settings



app = FastAPI()

@app.get('/')
def root():
    return {'masage': 'OK', 'settings': settings}


