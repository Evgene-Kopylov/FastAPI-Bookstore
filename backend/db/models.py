from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String
from sqlalchemy.sql.schema import Table
from sqlalchemy.orm import backref, relationship
from sqlalchemy.sql.sqltypes import DATE

from db.base_class import Base



book_author = Table('book_author',
    Base.metadata,
    Column('book_id', Integer, ForeignKey('book.id')),
    Column('author_id', Integer, ForeignKey('author.id'))
)


class Book(Base):
    id = Column(Integer,primary_key = True, index=True)
    title = Column(String,nullable= False)
    annotation = Column(String)
    isbn = Column(String)
    publish_at = Column(DATE)
    total_sells = Column(Integer, default=0)
    total_views = Column(Integer, default=0)
    authors = relationship(
        'Author',
        secondary=book_author,
        backref=backref('books', lazy='dynamic'))
    publisher_id = Column(
        Integer, 
        ForeignKey('publisher.id'))

class Author(Base):
    id = Column(Integer,primary_key = True, index=True)
    first_name = Column(String,nullable= False)
    last_name = Column(String)
    middle_name = Column(String)

class Publisher(Base):
    id = Column(Integer,primary_key = True, index=True)
    name = Column(String,nullable= False)
    description = Column(String,nullable= False)
    books = relationship(
        'Book',
        backref='publisher')
