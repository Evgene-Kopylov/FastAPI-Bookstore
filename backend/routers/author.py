from fastapi import APIRouter
from db.schemas.author import GetAuthor
from db.schemas.author import AuthorBase
from db.models import Book

from db.models import Author
from db.session import SessionLocal


db = SessionLocal()

router = APIRouter()



@router.post('/api/post/author/')
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

@router.get('/api/get/author/{author_id}', 
    response_model=GetAuthor)
def get_author(author_id: int):
    a = db.query(Author).get(author_id)
    books = db.query(Book).with_parent(a)

    items = books.order_by('publish_at').all()[::-1][:5]
    new_books = [item.__dict__ for item in items]

    items = books.order_by('total_sells').all()[::-1][:5]
    hot_books = [item.__dict__ for item in items]

    return {
        "id": a.id, # идентификатор автора
        "first_name": a.first_name, # имя автора
        "last_name": a.last_name, # фамилия автора
        "middle_name": a.middle_name, # отчество автора
        "books_total": 100, # кол-во опубликованных книг у автора
        "new_books": new_books,
        "hot_books": hot_books
    }
