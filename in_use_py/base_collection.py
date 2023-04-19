import inspect
from datetime import datetime

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker, scoped_session

from in_use_py.base_config import Base


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
    update_at = Column(String, default=datetime.utcnow, onupdate=datetime.utcnow)
    create_at = Column(String, default=datetime.utcnow)

    def __repr__(self):
        attributes = inspect.getmembers(self, lambda a: not(inspect.isroutine(a)))
        valid_attrs = [attr for attr in attributes if not(attr[0].startswith('_')) and attr[0] not in ('metadata', 'registry')]
        attr_str = ', '.join([f"{attr[0]}={attr[1]}" for attr in valid_attrs])
        return f"<{self.__class__.__name__}({attr_str})>"

    def to_dict(self):
        attributes = inspect.getmembers(self, lambda a: not(inspect.isroutine(a)))
        return {attr[0]: attr[1] for attr in attributes if not attr[0].startswith('_')}


class BaseDAO(metaclass=SingletonMeta):
    def __init__(self, model_class, engine):
        self.engine = engine
        self.model_class = model_class
        self.session_factory = sessionmaker(bind=engine)
        self.Session = scoped_session(self.session_factory)

    def create(self, obj):
        session = self.Session()
        try:
            session.add(obj)
            session.commit()
        finally:
            session.close()

    def read(self, id):
        session = self.Session()
        try:
            obj = session.query(self.model_class).get(id)
            return obj
        finally:
            session.close()

    def update(self, obj):
        session = self.Session()
        try:
            session.merge(obj)
            session.commit()
        finally:
            session.close()

    def delete(self, id):
        session = self.Session()
        try:
            obj = session.query(self.model_class).get(id)
            session.delete(obj)
            session.commit()
        finally:
            session.close()

    def query(self, *args, **kwargs):
        session = self.Session()
        try:
            result = session.query(self.model_class).filter(*args, **kwargs).all()
            return result
        finally:
            session.close()

    def update_item(self, filter_by, update_values):
        session = self.Session()
        try:
            session.query(self.model_class).filter_by(**filter_by).update(update_values)
            session.commit()
        finally:
            session.close()

