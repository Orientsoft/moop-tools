# -*- coding:utf-8 -*-
from pymongo import MongoClient
import config
from bson import ObjectId
from tenant import Tenant

connect = MongoClient(config.MONGODB_URI)


# 临时初始化工作，后续交给各自的用户实现
def temp():
    '''
        tag        ---   tenant admin
        category   --   super admin
        type       --   super admin
        租户管理员  --- super admin
    '''
    servicedb = connect[config.SERVICE_MONGODB_NAME]
    serverdb = connect[config.SERVER_MONGODB_NAME]
    # tag
    tags = [
        {
            "name": "基础学习",
            "delete": False
        },
        {
            "name": "编程学习",
            "delete": False
        },
        {
            "name": "自然科学",
            "delete": False
        },
        {
            "name": "金融科学",
            "delete": False
        }
    ]
    serverdb.tag.insert_many(tags)
    # category
    categorys = [
        {
            "_id": ObjectId("5c9dd3041bc17a4e031d254c"),
            "name": "数学",
            "delete": False
        },
        {
            "_id": ObjectId("5cada04c1bc17a4e032d3130"),
            "name": "信息科学与系统科学",
            "delete": False
        },
        {
            "_id": ObjectId("5cada0711bc17a4e032d3173"),
            "name": "基础医学",
            "delete": False
        },
        {
            "_id": ObjectId("5cada0831bc17a4e032d3193"),
            "name": "临床医学",
            "delete": False
        },
        {
            "_id": ObjectId("5cada0b21bc17a4e032d31ea"),
            "name": "工程与技术科学",
            "delete": False
        },
        {
            "_id": ObjectId("5cada0e81bc17a4e032d324f"),
            "name": "计算机科学技术",
            "delete": False
        },
        {
            "_id": ObjectId("5cada10c1bc17a4e032d328f"),
            "name": "航空、航天科学技术",
            "delete": False
        },
        {
            "_id": ObjectId("5cada1281bc17a4e032d32c4"),
            "name": "经济学",
            "delete": False
        },
        {
            "_id": ObjectId("5cada1401bc17a4e032d32ef"),
            "name": "统计学",
            "delete": False
        }]
    servicedb.category.insert_many(categorys)
    # type
    types = [
        {
            "_id": ObjectId("5cada2261bc17a4e032d34c8"),
            "category": ObjectId("5c9dd3041bc17a4e031d254c"),
            "name": "数理逻辑与数学基础",
            "delete": False
        },
        {
            "_id": ObjectId("5cada23b1bc17a4e032d34ef"),
            "category": ObjectId("5c9dd3041bc17a4e031d254c"),
            "name": "数学分析",
            "delete": False
        },
        {
            "_id": ObjectId("5cada24f1bc17a4e032d351b"),
            "category": ObjectId("5c9dd3041bc17a4e031d254c"),
            "name": "计算机数学",
            "delete": False
        },
        {
            "_id": ObjectId("5cada2601bc17a4e032d353b"),
            "category": ObjectId("5c9dd3041bc17a4e031d254c"),
            "name": "概率论",
            "delete": False
        },
        {
            "_id": ObjectId("5cada26d1bc17a4e032d3552"),
            "category": ObjectId("5c9dd3041bc17a4e031d254c"),
            "name": "应用数学",
            "delete": False
        },
        {
            "_id": ObjectId("5cada29a1bc17a4e032d35a7"),
            "category": ObjectId("5cada04c1bc17a4e032d3130"),
            "name": "信息科学与系统科学基础学科",
            "delete": False
        },
        {
            "_id": ObjectId("5cada2bc1bc17a4e032d35e8"),
            "category": ObjectId("5cada04c1bc17a4e032d3130"),
            "name": "系统工程方法论",
            "delete": False
        },
        {
            "_id": ObjectId("5cada2ca1bc17a4e032d3603"),
            "category": ObjectId("5cada04c1bc17a4e032d3130"),
            "name": "控制理论",
            "delete": False
        },
        {
            "_id": ObjectId("5cada3071bc17a4e032d3671"),
            "category": ObjectId("5cada0711bc17a4e032d3173"),
            "name": "医学生物化学",
            "delete": False
        },
        {
            "_id": ObjectId("5cada3161bc17a4e032d368d"),
            "category": ObjectId("5cada0711bc17a4e032d3173"),
            "name": "医学实验",
            "delete": False
        },
        {
            "_id": ObjectId("5cada4501bc17a4e032d38b3"),
            "category": ObjectId("5cada0e81bc17a4e032d324f"),
            "name": "人工智能",
            "delete": False
        },
        {
            "_id": ObjectId("5cada46d1bc17a4e032d38e0"),
            "category": ObjectId("5cada0e81bc17a4e032d324f"),
            "name": "计算机软件",
            "delete": False
        },
        {
            "_id": ObjectId("5cada5d31bc17a4e032d3b03"),
            "category": ObjectId("5cada1281bc17a4e032d32c4"),
            "name": "金融学",
            "delete": False
        },
        {
            "_id": ObjectId("5cada5df1bc17a4e032d3b18"),
            "category": ObjectId("5cada1281bc17a4e032d32c4"),
            "name": "信息经济学",
            "delete": False
        }]
    servicedb.type.insert_many(types)
    # 租户管理员
    serverdb.user.insert({
        "name": "admin",
        "key": "e35bece6c5e6e0e86ca51d0440e92282a9d6ac8a",
        "role": 2,
        "remark": "租户管理员",
        "invitation": "000000",
        "delete": False
    })


def addAdmin():
    db = connect[config.SERVER_MONGODB_NAME]
    db.user.insert({
        "name": "super",
        "key": "e35bece6c5e6e0e86ca51d0440e92282a9d6ac8a",
        "role": 0,
        "remark": "超级管理员",
        "invitation": "000000",
        "delete": False
    })


if __name__ == '__main__':
    # 租户初始化
    tenant = Tenant({'name': '测试租户', 'namespace': 'moop-test', 'remark': '测试租户的简介描述'})
    try:
        # 1.创建租户账号
        tenant.createTenant()
        # 2.增加pv
        tenant.addPV()
        # 3.增加PVC
        tenant.addPVC()
    except:
        print('租户创建失败，回滚')
        tenant.deleteTenant()
        tenant.deleteVoume()

    # 创建超级管理员
    addAdmin()

    # 初始化临时文件
    temp()
