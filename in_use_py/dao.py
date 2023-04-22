from typing import List

from sqlalchemy.orm import joinedload

from in_use_py.base_collection import BaseDAO
from in_use_py.model import Category, Device, TaskTemplate, Task, TaskSet, TaskSchedule


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


class TaskDao(BaseDAO):
    def __init__(self, engine):
        super().__init__(Task, engine)

    def add_task(self, name: str, params: dict, template_id: int, task_set_id: int) -> None:
        session = self.Session()
        try:
            template: TaskTemplate = session.query(TaskTemplate).get(template_id)
            task = Task(name=name, params=params, template_id=template_id, task_set_id=task_set_id, template_version=template.version)
            session.add(task)
            session.commit()
        finally:
            session.close()

    def query_task_with_joined(self, id: int)-> Task:
        self.query()


class TaskSetDao(BaseDAO):
    def __init__(self, engine):
        super().__init__(TaskSet, engine)

    def add_task_set(self, name: str) -> None:
        session = self.Session()
        try:
            task_set = TaskSet(name=name)
            session.add(task_set)
            session.commit()
        finally:
            session.close()


class TaskScheduleDao(BaseDAO):
    def __init__(self, engine):
        super().__init__(TaskSchedule, engine)

    def add_task_schedule(self, name: str) -> None:
        session = self.Session()
        try:
            task_schedule = TaskSchedule(name=name)
            session.add(task_schedule)
            session.commit()
        finally:
            session.close()

    # 联表添加


