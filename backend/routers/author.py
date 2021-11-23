from fastapi import APIRouter

from fastapi import status
from fastapi import Response

from db.schemas.author import PATCH_author
from db.schemas.author import ListAuthor
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
        'msg': 'OK',
        'data': request,
        'authors_list': authors_list
    }

@router.get('/api/get/author/{author_id}', 
    response_model=GetAuthor)
def get_author(author_id: int):
    a = db.query(Author).get(author_id)
    books = db.query(Book).with_parent(a)

    books_total = books.count()

    items = books.order_by('publish_at').all()[::-1][:5]
    new_books = [item.__dict__ for item in items]

    items = books.order_by('total_sells').all()[::-1][:5]
    hot_books = [item.__dict__ for item in items]

    return {
        "id": a.id,
        "first_name": a.first_name,
        "last_name": a.last_name,
        "middle_name": a.middle_name,
        "books_total": books_total,
        "new_books": new_books,
        "hot_books": hot_books
    }


@router.get('/api/get/author/', response_model=ListAuthor)
def list_authors(page:int, size:int):
    authors = db.query(Author)
    total = authors.count()

    i = total - (page * size)
    if i < 0: i = 0
    k = i + size

    authors = authors.all()
    items = []    
    for author in authors:
        item = author.__dict__
        item.update({'books_total':author.books.count()})
        items.append(item)

    items = sorted(items, key=lambda d: d['books_total'])[i:k][::-1]


    return {
        "items": items,
        "total": total,
        "page": page,
        "size": size
    }


@router.patch('/api/patch/author/{author_id}')
def update_author(author_id:int, request: PATCH_author):
    author = db.query(Author).get(author_id)
    if request.first_name:
        author.first_name = request.first_name
    if request.last_name:
        author.last_name = request.last_name
    if request.middle_name:
        author.middle_name = request.middle_name

    db.commit()
    db.refresh(author)
    return author


@router.delete('/api/delete/author/{author_id}')
def delete_author(author_id:int, response: Response):
    author = db.query(Author).get(author_id)
    if author is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'messege': 'author not found'}
    db.delete(author)
    db.commit()
    return {'messege': 'author deleted'}

