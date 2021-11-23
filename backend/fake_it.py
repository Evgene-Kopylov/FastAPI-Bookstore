from tests.bookstore_faker import BookstoreFactory

factory = BookstoreFactory()

if __name__ == "__main__":
    factory.fake_all(10,50,100)

