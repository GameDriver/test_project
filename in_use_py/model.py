from sqlalchemy import String
from sqlalchemy.testing.schema import Column

from in_use_py.base_collection import BaseModel
from in_use_py.base_config import Base, engine


class Category(BaseModel):
    __tablename__ = 'Category'

    name = Column(String, nullable=False)


class Device(BaseModel):
    __tablename__ = 'Device'

    # serial = Column(String, nullable=False)


Base.metadata.create_all(engine)
