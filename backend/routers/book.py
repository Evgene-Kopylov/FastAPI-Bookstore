from fastapi import APIRouter
from db.base_models import BookBase
from db.models import Book
from db.session import SessionLocal

from db.base_models import AuthorBase
from db.models import Author


db = SessionLocal()

router = APIRouter()


@router.post('/api/post/book/')
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


@router.get('/api/get/book/')
def list_books():
    books = db.query(Book).all()[::-1][:5]
    return books


@router.get('/api/get/book/{book_id}')
def get_book(book_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()
    return book

