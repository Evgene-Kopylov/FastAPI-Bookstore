from fastapi import FastAPI
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)



def test_get_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "settings" in response.json().keys()

def test_get_book_all():
    response = client.get('/api/get/book/')
    assert response.status_code == 200

def test_get_book_book_id():
    response = client.get('/api/get/book/1')
    assert response.status_code == 200
    print(response.json())
    assert "title" in response.json().keys()

def test_post_book():
    body = {
        "title": "SSS"
    }    
    response = client.post('/api/get/book/', body)
    assert response.status_code == 200




