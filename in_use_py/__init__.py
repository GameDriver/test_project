import time

from in_use_py.base_config import engine
from in_use_py.dao import CategoryDao, DeviceDao, TaskTemplateDao

category_dao = CategoryDao(engine)

device_dao = DeviceDao(engine)

task_template_dao = TaskTemplateDao(engine)

# category_dao = CategoryDao()

if __name__ == '__main__':
    ...
    # cate_dao = CategoryDao(engine)
    # # create a new category
    # cate_dao.add_cate("test_category", "a test category")
    #
    # # retrieve a category and print it
    # cate = cate_dao.get_category_with_devices(1)
    # print(cate)
    #
    # # retrieve devices associated with the category and print them
    # devices = cate.devices
    # print(devices)
    #
    # cate_list = cate_dao.get_all_category_with_devices()
    # print('cate_list')
    # print(cate_list)
    #
    # device_dao.add_device('test serial 2', 'my device', cate.id)
    # d = device_dao.read(1)
    # print('test d')
    # print(d)
    # struct = {
    #     'total_time': {
    #         'desc': '总时间',
    #         'type': 'range',
    #         'unit': '分钟'
    #     }
    #
    # }
    # task_template_dao.add_template('dy1', struct)

    # todo ① 添加任务模板
    # todo ② 查询任务模板
    # todo ③ 添加任务集
    # todo ④ 添加任务×2
    # todo ⑤ 查询任务集-根据id——获取对应
    # todo ⑥ 查询任务-根据id——获取对应模板、对应任务集
    # todo ⑦ 添加任务日程
    # todo ⑧ 查询任务日程-通过id
    # todo ⑨ 查询任务集-获取所有in_use的任务集——包含对应任务、排序
    # todo ⑩ 查询任务-根据id——获取对应模板、对应任务集
    # todo  查询任务-根据id——获取对应模板、对应任务集


