from db import db_dao

if __name__ == '__main__':
    print('123')

    # 1. 插入 设备分类
    db_dao.device_cate_insert('device cate 1')
    # 2. 查询 设备分类
    cate = db_dao.device_cate_get(1)
    print(cate)
    # 3. 修改 设备分类 名称
    db_dao.device_cate_update(1, 'device cate 1 update name')
    # 4. 删除 设备分类
    # db_dao.device_cate_delete(1)
