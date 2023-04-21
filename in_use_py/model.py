from sqlalchemy import String, Column, Integer, ForeignKey, Boolean
from sqlalchemy.dialects.sqlite import JSON
from sqlalchemy.orm import relationship

from in_use_py.base_collection import BaseModel
from in_use_py.base_config import Base, engine


class Category(BaseModel):
    __tablename__ = 'Category'

    name = Column(String, nullable=False)
    devices = relationship("Device", back_populates="category")


class Device(BaseModel):
    __tablename__ = 'Device'

    serial = Column(String, nullable=False)
    category_id = Column(Integer, ForeignKey('Category.id'), nullable=True, default=None)  # 添加外键
    category = relationship("Category", back_populates="devices")


# 任务模板表
class TaskTemplate(BaseModel):
    __tablename__ = 'TaskTemplate'

    name = Column(String, nullable=False)
    struct = Column(JSON, nullable=False)
    version = Column(Integer, nullable=False, default=1)

    tasks = relationship("Task", back_populates="template")


# 任务表
class Task(BaseModel):
    __tablename__ = 'Task'

    name = Column(String, nullable=False)
    in_use = Column(Boolean, default=True)
    params = Column(String, nullable=False)
    template_id = Column(Integer, ForeignKey('TaskTemplate.id'), nullable=False)  # 添加外键
    task_set_id = Column(Integer, ForeignKey('TaskSet.id'), nullable=False)  # 添加外键
    template_version = Column(Integer, nullable=False)

    template = relationship("TaskTemplate", back_populates="tasks")
    task_set = relationship("TaskSet", back_populates="tasks")


# 任务集表
class TaskSet(BaseModel):
    __tablename__ = 'TaskSet'

    name = Column(String, nullable=False)

    tasks = relationship("Task", back_populates="template")


# 任务计划表
# class TaskSchedule(BaseModel):
#     __tablename__ = 'TaskSet'
#
#     name = Column(String, nullable=False)
#
#     tasks = relationship("Task", back_populates="template")


Base.metadata.create_all(engine)
