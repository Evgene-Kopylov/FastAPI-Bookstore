from fastapi import FastAPI
import uvicorn

from core.config import settings
from db.base import Base
from db.session import engine



def create_tables():
	print("create_tables")
	Base.metadata.create_all(bind=engine)

def start_application():
	app = FastAPI(title=settings.project_name,version=settings.project_version)
	create_tables()
	return app


app = start_application()

@app.get('/')
def root():
    return {'settings': settings}



if __name__ == "__main__":
    uvicorn.run(
        "main:app", 
        host="0.0.0.0", 
        port=8000, 
        reload=True)
    