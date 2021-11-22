from fastapi import APIRouter
from db.models import Publisher
from db.models import Author
from db.models import Book
from db.session import SessionLocal

from db import schemas


db = SessionLocal()

router = APIRouter()


@router.post('/api/post/book/')
def add_book(request: schemas.Book):
    b = Book()
    b.title = request.title
    for author_id in request.authors:
        author = db.query(Author).get(author_id)
        b.authors.append(author)
    publisher = db.query(Publisher).get(request.publisher_id)
    b.publisher = publisher
    db.add(b)

    db.commit()
    db.refresh(b)
    db.refresh(publisher)

    books_list = db.query(Book).all()[::-1][:5]

    return {
        'msg': "msg",
        'data': request,
        'books_list': books_list
    }


@router.get('/api/get/book/')
def list_books():
    books = db.query(Book).all()[::-1][:5]
    return books


@router.get('/api/get/book/{book_id}')
def get_book(book_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()
    return book

