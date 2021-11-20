from backend.core.config import settings
from fastapi import FastAPI
from sqlalchemy.orm import query
from sqlalchemy.orm.session import Session
import uvicorn
from backend.db.session import SessionLocal
from backend.db.models import Book


from backend.db.base import Base
from backend.db.base import BookSchema

from backend.db.session import engine


db = SessionLocal()


# def create_tables():
# 	print("create_tables")
# 	Base.metadata.create_all(bind=engine)

def start_application():
	app = FastAPI(
        title=settings.project_name,
        version=settings.project_version)
	# create_tables()
	return app


app = start_application()

@app.get('/')
def root():
    return {'settings': settings}


@app.post('/api/post/book/')
def add_book(data: BookSchema):
    obj = Book(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)

    all_books = db.query(Book).all()[::-1]

    return {
        'msg': 'book',
        'data': data,
        'all_books': all_books
    }


@app.get('/api/get/book/')
def list_books():
    books = db.query(Book).all()[::-1][:5]
    return books


@app.get('/api/get/book/{book_id}')
def get_book(book_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()
    return book




if __name__ == "__main__":
    uvicorn.run(
        "main:app", 
        host="0.0.0.0", 
        port=8000, 
        reload=True)
    