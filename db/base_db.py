import inspect
from datetime import datetime
from typing import Type

from sqlalchemy import Column, Integer, String, update
from sqlalchemy.orm import sessionmaker, scoped_session, joinedload

from .base_config import Base
from .model import engine
from .model import Category


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class BaseModel(Base):
    __abstract__ = True  # 将这个类声明为抽象类
    id = Column(Integer, primary_key=True)
    desc = Column(String, default=None)
    update_at = Column(String, default=datetime.now, onupdate=datetime.now)
    create_at = Column(String, default=datetime.now)

    def to_dict(self):
        attributes = inspect.getmembers(self, lambda a: not(inspect.isroutine(a)))
        return {attr[0]: attr[1] for attr in attributes if not attr[0].startswith('_')}


class BaseDAO(metaclass=SingletonMeta):
    def __init__(self, engine):
        self.engine = engine
        self.session_factory = sessionmaker(bind=engine)
        self.Session = scoped_session(self.session_factory)

    def create(self, obj):
        session = self.Session()
        try:
            session.add(obj)
            session.commit()
        finally:
            session.close()

    def update(self, obj):
        session = self.Session()
        try:
            session.merge(obj)
            session.commit()
        finally:
            session.close()

    def delete(self, model_class: Type[BaseModel], id):
        session = self.Session()
        try:
            obj = session.query(model_class).get(id)
            session.delete(obj)
            session.commit()
        finally:
            session.close()

    def device_cate_insert(self, name):
        cate = Category(name=name)
        self.create(cate)

    def device_cate_update(self, id, name):
        session = self.Session()
        try:
            stmt = update(Category).where(Category.id == id).values(name=name)
            session.execute(stmt)
            session.commit()
        finally:
            session.close()

    def device_cate_delete(self, id):
        self.delete(Category, id)

    def device_cate_get(self, id, join_load: bool = False):
        session = self.Session()
        try:
            if join_load:
                result = session.query(Category).options(joinedload(Category.devices)).get(id)
            else:
                result = session.query(Category).get(id)
            return result
        finally:
            session.close()

    def device_cate_get_all(self, join_load: bool = False):
        session = self.Session()
        try:
            if join_load:
                result = session.query(Category).options(joinedload(Category.devices)).all()
            else:
                result = session.query(Category).all()
            return result
        finally:
            session.close()
