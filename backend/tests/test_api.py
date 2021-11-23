from fastapi.testclient import TestClient

from main import app

client = TestClient(app)



def test_get_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "settings" in response.json().keys()



def test_get_book_book_list():
    response = client.get('/api/get/book/?page=1&size=10')
    assert response.status_code == 200

def test_get_book_book_id():
    response = client.get('/api/get/book/1')
    assert response.status_code == 200
    assert "title" in response.json().keys()


# def test_get_author_author_list():
#     response = client.get('/api/get/author/')
#     assert response.status_code == 200


def test_get_author_author_id():
    response = client.get('/api/get/author/1')
    assert response.status_code == 200
    assert "first_name" in response.json().keys()


def test_get_publisher_publisher_list():
    response = client.get('/api/get/publisher/?page=1&size=3')
    assert response.status_code == 200

def test_get_publisher_publisher_id():
    response = client.get('/api/get/publisher/1')
    assert response.status_code == 200
    print(response.json())
    assert "name" in response.json().keys()



# def test_post_book():
#     data = {
#         "title": "SSD",
#         "authors": [1,2],
#         "publisher": 1
#     }
#     response = client.post('/api/get/book/', data)
#     assert response.status_code == 200




