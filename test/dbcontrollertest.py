from typing import Optional

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, Mapped, mapped_column

db_url = 'mysql+mysqldb://sql12737141:J4SDu1KBvf@sql12.freesqldatabase.com:3306/sql12737141'
# db_url = 'mysql://sql12737141:J4SDu1KBvf@sql12.freesqldatabase.com:3306/testdb.db'

engine = create_engine(db_url)

connection = engine.connect() #! น่าจะต้องสั่ง engine.connect

print('engine created')

Base = declarative_base()

# class User(Base):
#     __tablename__ = 'users'

#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     age = Column(Integer)


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    fullname: Mapped[Optional[str]]
    nickname: Mapped[Optional[str]] = mapped_column(String(30))

# Base.metadata.create_all(engine)

connection.execute()