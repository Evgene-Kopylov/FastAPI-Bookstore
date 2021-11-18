from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String
# from sqlalchemy.orm import relationship

from db.base_class import Base


class Book(Base):
    id = Column(Integer,primary_key = True, index=True)
    title = Column(String,nullable= False)
