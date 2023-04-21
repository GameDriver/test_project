from typing import List

from sqlalchemy.orm import joinedload

from in_use_py.base_collection import BaseDAO
from in_use_py.model import Category, Device, TaskTemplate


class CategoryDao(BaseDAO):
    def __init__(self, engine):
        super().__init__(Category, engine)

    def add_cate(self, name, desc) -> None:
        cate = Category(name=name, desc=desc, devices=[])
        self.create(cate)

    def get_all_cate(self) -> List[Category]:
        session = self.Session()
        try:
            return session.query(Category).all()
        finally:
            session.close()

    def update_cate_name(self, cate_id, name) -> None:
        session = self.Session()
        try:
            cate: Category = session.query(Category).filter(Category.id == cate_id).first()
            if cate:
                cate.name = name
                session.commit()
        finally:
            session.close()

    def get_all_category_with_devices(self) -> List[Category]:
        session = self.Session()
        try:
            return session.query(Category).options(joinedload(Category.devices)).all()
        finally:
            session.close()

    # 在CategoryDao类中添加一个方法来获取Category及其关联的devices
    def get_category_with_devices(self, id) -> Category:
        session = self.Session()
        try:
            category = session.query(Category).options(joinedload(Category.devices)).get(id)
            return category
        finally:
            session.close()


class DeviceDao(BaseDAO):
    def __init__(self, engine):
        super().__init__(Device, engine)
    ...

    def add_device(self, serial, desc, category_id) -> None:
        device = Device(serial=serial, desc=desc, category_id=category_id)
        self.create(device)


class TaskTemplateDao(BaseDAO):
    def __init__(self, engine):
        super().__init__(TaskTemplate, engine)

    def add_template(self, name: str, struct: dict) -> None:
        TaskTemplate(name=name, struct=struct)
        self.create(TaskTemplate)
