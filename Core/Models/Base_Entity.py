from email.mime import base
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

@as_declarative()
class Base:
     __abstract__ = True
     __name__: str

     @declared_attr.directive
     def __tablename__(cls) -> str:
         return cls.__name__.lower()
     


class BareBaseModel(Base):
    __abstract__ = True

    Id : Mapped[int] = mapped_column(primary_key = True, autoincrement = True)
    Created_at : Mapped[datetime] = mapped_column(default=datetime.now)
    Cpdated_at : Mapped[datetime] = mapped_column(default=datetime.now, onupdate=datetime.now)