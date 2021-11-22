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
    books = Book.o.filter()


    return {
        "id": a.id, # идентификатор автора
        "first_name": a.first_name, # имя автора
        "last_name": a.last_name, # фамилия автора
        "second_name": a.second_name, # отчество автора
        "books_total": 100, # кол-во опубликованных книг у автора
        "new_books": [ # список новых книг, не более 5 шт.
            {
                "id": 1, # идентификатор книги
                "title": "Book title", # заголовок книги
                "annotation": "Book annotation...", # краткое изложение книги
                "publish_at": "2021-02-28", # дата публикации
                "total_sells": 100, # кол-во продаж
                "total_views": 10000 # кол-во просмотров
            }
        ],
        "hot_books": [ # список самых продаваемых книг, не более 5 шт.
            {
                "id": 1, # идентификатор книги
                "title": "Book title", # заголовок книги
                "annotation": "Book annotation...", # краткое изложение книги
                "publish_at": "2021-02-28", # дата публикации
                "total_sells": 100, # кол-во продаж
                "total_views": 10000 # кол-во просмотров
            }
        ]
    }