from fastapi import APIRouter
from db.schemas import publisher
from db.schemas.publisher import ListPublisher
from db.schemas.publisher import GetPublisher
from db.models import Book
from db.session import SessionLocal
from db.models import Publisher

from db.schemas.publisher import PublisherBase


db = SessionLocal()

router = APIRouter()


@router.post('/api/post/publisher/')
def add_publisher(request: PublisherBase):
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


@router.get('/api/get/publisher/{publisher_id}',
    response_model=GetPublisher)
def get_publisher(publisher_id: int):
    p = db.query(Publisher).get(publisher_id)
    books = db.query(Book).filter(Book.publisher_id==p.id)

    items = books.order_by('publish_at').all()[::-1][:5]
    new_books = [item.__dict__ for item in items]

    items = books.order_by('total_sells').all()[::-1][:5]
    hot_books = [item.__dict__ for item in items]

    return {
        "id": p.id, # идентификатор издателя
        "name": p.name, # имя издателя
        "description": p.description, # описание издателя
        "books_total": len(books.all()), # кол-во напечатанных книг этим издателем
        "new_books": new_books,
        "hot_books": hot_books
    }


@router.get("/api/get/publisher/", 
    response_model=ListPublisher)
def list_publishers(page:int, size:int):
    publishers = db.query(Publisher)
    total = publishers.count()

    i = total - (page * size)
    if i < 0: i = 0
    k = i + size

    publishers = publishers.order_by('id').all()
    items = []    
    for p in publishers:
        item = p.__dict__
        item.update({'books_total':len(p.books)})
        items.append(item)

    items = sorted(items, key=lambda d: d['books_total'])[i:k][::-1]

    return {
        "items": items,
        "total": total,
        "page": page,
        "size": size
    }


