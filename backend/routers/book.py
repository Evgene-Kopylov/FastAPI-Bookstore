from fastapi import APIRouter
from db.schemas.book import BookBase
from db.schemas.book import ListBooks
from db.models import Publisher
from db.models import Author
from db.models import Book
from db.session import SessionLocal


db = SessionLocal()

router = APIRouter()


@router.post('/api/post/book/')
def add_book(request: BookBase):
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


@router.get('/api/get/book/', response_model=ListBooks)
def list_books(page:int, size:int):
    books = db.query(Book)
    total = books.count()

    i = total - (page * size)
    if i < 0: i = 0
    k = i + size

    raw_items = books.order_by('total_views').all()[i:k][::-1]

    items = [item.__dict__ for item in raw_items]

    return {
        "items": items,
        "total": total,
        "page": page,
        "size": size
    }



@router.get('/api/get/book/{book_id}')
def get_book(book_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()
    return {
        "id": 1, # идентификатор книги
        "title": "Book title", # заголовок книги
        "annotation": "Book annotation...", # краткое изложение книги
        "isbn": "9783161484100",
        "publish_at": "2021-02-28", # дата публикации
        "total_sells": 100, # кол-во продаж
        "total_views": 10000, # кол-во просмотров
        "authors": [ # полный список авторов книги
            {
                "id": 1, # идентификатор автора
                "first_name": "Александр", # имя автора
                "last_name": "Пушкин", # фамилия автора
                "second_name": "Сергеевич", # отчество автора
            }
        ],
        "publisher": {
            "id": 1, # идентификатор издателя
            "name": "Publisher", # имя издателя
        }
    }

