from db.base_models import AuthorBase
from db.models import Author
from core.config import settings
from fastapi import FastAPI
from sqlalchemy.orm import query
from sqlalchemy.orm.session import Session
import uvicorn
from db.session import SessionLocal
from db.models import Book


from db.base import Base
from db.base import BookBase

from db.session import engine


db = SessionLocal()


def start_application():
	app = FastAPI(
        title=settings.project_name,
        version=settings.project_version)
	return app


app = start_application()


@app.get('/')
def root():
    return {'settings': settings}

@app.post('/api/post/author/')
def add_author(request: AuthorBase):
    obj = Author(**request.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)

    authors_list = db.query(Author).all()[::-1][:5]

    return {
        'msg': 'msg',
        'data': request,
        'authors_list': authors_list
    }

@app.post('/api/post/book/')
def add_book(request: BookBase):
    b = Book()
    b.title = request.title
    for author_id in request.authors:
        author = db.query(Author).get(author_id)
        b.authors.append(author)
    db.add(b)
    db.commit()
    db.refresh(b)

    books_list = db.query(Book).all()[::-1][:5]

    return {
        'msg': "msg",
        'data': request,
        'books_list': books_list
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
    