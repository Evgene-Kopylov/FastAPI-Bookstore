from fastapi import APIRouter
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






@router.get("/api/get/publisher/")
def list_publishers():
    return {"router": "publisher"}


