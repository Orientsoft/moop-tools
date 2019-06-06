# -*- coding:utf-8 -*-
from pymongo import MongoClient
import config
from bson import ObjectId

connect = MongoClient(config.MONGODB_URI)


# 创建一级分类和相应的二级分类
def CategoryAndType(data):
    servicedb = connect[config.SERVICE_MONGODB_NAME]
    # category
    for d in data:
        categoryid = ''
        category = servicedb.category.find_one({'name':d['category']})
        if category:
            categoryid = category['_id']
        else:
            id = servicedb.category.insert({'name':d['category'],'delete':False})
            categoryid = ObjectId(id)
        types = []
        for x in d['type']:
            status = servicedb.type.find_one({'name':x})
            if not status:
                types.append({
                    'category':categoryid,
                    'name':x,
                    'delete':False
                })
        if types:
            servicedb.type.insert_many(types)
    return '创建成功'

if __name__ == '__main__':
    # 创建分类
    data = [
        {'category': '通信工程', 'type': ['四川电信', '重庆电信']},
        {'category': '土木工程', 'type': ['道路桥梁','艺术设计']}
    ]
    result = CategoryAndType(data)
    print(result)
