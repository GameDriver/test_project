from sqlalchemy import String, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from in_use_py.base_collection import BaseModel
from in_use_py.base_config import Base, engine


class Category(BaseModel):
    __tablename__ = 'Category'

    name = Column(String, nullable=False)
    # devices = relationship("Device", back_populates="category")  # 添加关联关系
    # devices = relationship("Device", uselist=True, backref='category')  # 添加关联关系
    # devices = relationship("Device", back_populates="category", lazy="joined")  # 更改加载策略为立即加载
    devices = relationship("Device", back_populates="category")


class Device(BaseModel):
    __tablename__ = 'Device'

    serial = Column(String, nullable=False)
    category_id = Column(Integer, ForeignKey('Category.id'), nullable=True, default=None)  # 添加外键
    category = relationship("Category", back_populates="devices")


Base.metadata.create_all(engine)
