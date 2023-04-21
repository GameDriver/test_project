import time

from in_use_py.base_config import engine
from in_use_py.dao import CategoryDao, DeviceDao

category_dao = CategoryDao(engine)

device_dao = DeviceDao(engine)

# category_dao = CategoryDao()

if __name__ == '__main__':
    category_dao.add_cate('typeggg', 'descxxx')

    cate = category_dao.query()

    print(cate)

    device_dao.add_device('123456789xxx', 'descxxx', 1)

    devices = device_dao.query()

    print(devices)

    time.sleep(4)

    device = devices[0]
    device.desc = 's111'
    device_dao.update(device)

    devices = device_dao.query()

    print(devices)

