from fastapi import APIRouter

router = APIRouter()

@router.get("/api/get/publisher/")
def list_publishers():
    return {"router": "publisher"}