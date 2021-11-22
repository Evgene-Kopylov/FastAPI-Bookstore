from fastapi import APIRouter
from db.models import Book
from db.session import SessionLocal
from db.models import Author
from db.models import Publisher

from db import schemas


db = SessionLocal()

router = APIRouter()


@router.post('/api/post/publisher/')
def add_publisher(request: schemas.Publisher):
    p = Publisher()
    p.name = request.name
    db.add(p)
    db.commit()
    db.refresh(p)

    publishers_list = db.query(Publisher).all()[::-1][:5]

    return {
        'msg': "publisher",
        'data': request,
        'publishers_list': publishers_list
    }


@router.get('/api/post/publisher/{publisher_id}')
def get_publisher(publisher_id: int):
    p = db.query(Publisher).get(publisher_id)
    books = db.query(Book).filter(publisher_id==p.id)
    new_books = books.order_by('publish_at').all()[::-1][:5]
    hot_books = books.order_by('total_sells').all()[::-1][:5]
    return {
        "id": p.id, # идентификатор издателя
        "name": p.name, # имя издателя
        "description": p.description, # описание издателя
        "books_total": len(books.all()), # кол-во напечатанных книг этим издателем
        "new_books": new_books,
        # [ # список новых книг, не более 5 шт.
        #     {
        #         "id": 1, # идентификатор книги
        #         "title": "Book title", # заголовок книги
        #         "annotation": "Book annotation...", # краткое изложение книги
        #         "publish_at": "2021-02-28", # дата публикации
        #         "total_sells": 100, # кол-во продаж
        #         "total_views": 10000 # кол-во просмотров
        #     }
        # ],
        "hot_books": hot_books
        # [ # список самых продаваемых книг, не более 5 шт.
        #     {
        #         "id": 1, # идентификатор книги
        #         "title": "Book title", # заголовок книги
        #         "annotation": "Book annotation...", # краткое изложение книги
        #         "publish_at": "2021-02-28", # дата публикации
        #         "total_sells": 100, # кол-во продаж
        #         "total_views": 10000 # кол-во просмотров
        #     }
        # ]
    }




@router.get("/api/get/publisher/")
def list_publishers():
    return {"router": "publisher"}


