
import datetime
import random
from db.models import Author, Book
from db.models import Publisher
from db.session import SessionLocal
from faker import Faker



class BookstoreFactory:
    def __init__(self):
        self.fake = Faker('Ru_RU')
        self.db = SessionLocal()

    def fake_all(self, n_publishers, n_authors, n_books):
        for _ in range(n_publishers):
            publisher = self.fake_publisher()
            self.db.add(publisher)
        self.db.commit()
        
        for _ in range(n_authors):
            author = self.fake_author()
            self.db.add(author)
        self.db.commit()

        for _ in range(n_books):
            book = self.fake_book()
            self.db.add(book)
        self.db.commit()


    def fake_publisher(self):
        publisher = Publisher()
        publisher.name = self.fake.sentence(nb_words=1)
        publisher.description = self.fake.sentence(nb_words=15)
        return publisher


    def fake_author(self):
        a = Author()
        a.first_name = self.fake.first_name()
        a.last_name = self.fake.last_name()
        a.middle_name = self.fake.middle_name()
        return a


    def fake_book(self):
        b = Book()
        b.title = self.fake.sentence(nb_words=4)
        b.annotation = self.fake.sentence(nb_words=15)
        b.isbn = self.fake.isbn13()
        b.publish_at = self.fake.date_between(
            datetime.date.today() - datetime.timedelta(days=5000),
            datetime.date.today())
        b.total_sells = self.fake.pyint(0,100,1)
        b.total_views = self.fake.pyint(0,10000,1)
        
        authors = self.db.query(Author).all()
        for _ in range(self.fake.pyint(1,3,1)):
            author = random.choice(authors)
            b.authors.append(author)
        
        publishers = self.db.query(Publisher).all()
        b.publisher_id = random.choice(publishers).id
        return b

        
