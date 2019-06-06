# -*- coding:utf-8 -*-
from pymongo import MongoClient
import config

connect = MongoClient(config.MONGODB_URI)


def addSuper(user):
    db = connect[config.SERVER_MONGODB_NAME]
    user = db.user.find_one({'$or': [{'name': user['username']}, {'invitation': user['invitation']}]})
    if user:
        return '用户名或邀请码已存在'
    db.user.insert({
        "name": user['username'],
        "key": "e35bece6c5e6e0e86ca51d0440e92282a9d6ac8a",
        "role": 0,
        "remark": "超级管理员",
        "invitation": user['invitation'],
        "delete": False
    })
    return '创建成功'


if __name__ == '__main__':
    # 创建超级管理员
    result = addSuper({'username': 'super', 'invitation': '000000'})
    print(result)