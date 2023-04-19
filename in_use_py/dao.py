from in_use_py.base_collection import BaseDAO
from in_use_py.model import Category, Device


class CategoryDao(BaseDAO):
    def __init__(self, engine):
        super().__init__(Category, engine)

    def add_cate(self, name, desc):
        cate = Category(desc=desc)
        self.create(cate)

    def get_all_cate(self):
        session = self.Session()
        try:
            return session.query(Category).all()
        finally:
            session.close()

    def update_cate_name(self, cate_id, name):
        session = self.Session()
        try:
            cate: Category = session.query(Category).filter(Category.id == cate_id).first()
            if cate:
                cate.name = name
                session.commit()
        finally:
            session.close()


class DeviceDao(BaseDAO):
    def __init__(self, engine):
        super().__init__(Device, engine)
    ...

