from fastapi import APIRouter

from db.base_models import AuthorBase
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