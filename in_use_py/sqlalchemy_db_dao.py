from concurrent.futures import ThreadPoolExecutor
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "sqlite:///my_database.db"

engine = create_engine(DATABASE_URL)

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)


def add_user(name, age):
    session = Session()
    try:
        new_user = User(name=name, age=age)
        session.add(new_user)
        session.commit()
    finally:
        session.close()


def get_users():
    session = Session()
    try:
        users = session.query(User).all()
        return users
    finally:
        session.close()


def concurrent_operations(operations, max_workers=10):
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = list(executor.map(lambda f: f(), operations))
    return results


def main():
    # 添加测试数据
    operations = [lambda: add_user(f"User {i}", i) for i in range(70)]
    concurrent_operations(operations, max_workers=10)

    # 获取用户
    operations = [get_users for _ in range(100)]
    results = concurrent_operations(operations, max_workers=10)

    # 输出结果
    for users in results:
        for user in users:
            print(user.id, user.name, user.age)


if __name__ == "__main__":
    main()
