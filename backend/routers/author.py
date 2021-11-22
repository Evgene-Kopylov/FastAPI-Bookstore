from fastapi import APIRouter
from db.models import Book

from db import schemas
from db.models import Author
from db.session import SessionLocal


db = SessionLocal()

router = APIRouter()



@router.post('/api/post/author/')
def add_author(request: schemas.Author):
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

@router.get('/api/post/author/{author_id}')
def get_author(author_id: int):
    a = db.query(Author).get(author_id)
    books = db.query(Book).with_parent(a)
    new_books = books.order_by('publish_at').all()[::-1][:5]
    hot_books = books.order_by('total_sells').all()[::-1][:5]

    return {
        "id": a.id, # идентификатор автора
        "first_name": a.first_name, # имя автора
        "last_name": a.last_name, # фамилия автора
        "middle_name": a.middle_name, # отчество автора
        "books_total": 100, # кол-во опубликованных книг у автора
        "new_books": new_books,
        "hot_books": hot_books
    }