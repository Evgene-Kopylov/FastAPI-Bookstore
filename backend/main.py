from core.config import settings
from fastapi import FastAPI

import uvicorn
from db.session import SessionLocal

from routers import publisher
from routers import author
from routers import book


db = SessionLocal()


def start_application():
	app = FastAPI(
        title=settings.project_name,
        version=settings.project_version)
	return app


app = start_application()


app.include_router(publisher.router)
app.include_router(author.router)
app.include_router(book.router)


@app.get('/')
def root():
    return {'settings': settings}


if __name__ == "__main__":
    uvicorn.run(
        "main:app", 
        host="0.0.0.0", 
        port=8000, 
        reload=True)
    