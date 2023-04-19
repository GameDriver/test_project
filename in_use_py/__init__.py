from in_use_py.base_config import engine
from in_use_py.dao import CategoryDao, DeviceDao

category_dao = CategoryDao(engine)

device_dao = DeviceDao(engine)

# category_dao = CategoryDao()

if __name__ == '__main__':
    category_dao.add_cate('type1', 'descxxx')

    cate = category_dao.query()

    print(cate)
