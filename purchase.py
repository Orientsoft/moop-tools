# -*- coding:utf-8 -*-
from pymongo import MongoClient
import config
from bson import ObjectId
import datetime

connect = MongoClient(config.MONGODB_URI)
servicedb = connect[config.SERVICE_MONGODB_NAME]


# 创建purchase
def purchaseAdd(data):
    project = servicedb.project.find_one({'_id': data['project'],"delete": False})
    if not project:
        return '购买的project不存在'
    tenant = servicedb.tenant.find_one({'_id': data['purchaser'],"delete": False})
    if not tenant:
        return '租户不存在'
    servicedb.purchase.insert(data)
    return '创建成功'


def getProject():
    projects = servicedb.project.find({"delete": False})
    for p in projects:
        print('project编号：{}，标题：{}，github地址：{}'.format(str(p['_id']), str(p['title']), str(p['spec'])))


def getTenant():
    tenants = servicedb.tenant.find({"delete": False})
    for t in tenants:
        print('租户编号：{}，名称：{}，namespace：{}'.format(str(t['_id']), str(t['name']), str(t['namespace'])))


if __name__ == '__main__':
    # 拉取所有的租户
    print('=' * 30)
    print('所有租户信息如下：')
    getTenant()
    tenant = raw_input('请输入购买的租户编号，：')
    # 拉取所有的project
    print('=' * 30)
    print('所有的project信息如下：')
    getProject()
    projectid = raw_input('请输入购买的project编号：')
    # limit时间
    limit = raw_input('请输入购买到期时间，格式：2019-05-23  ：')
    try:
    # 购买purchase
        data = {
            "purchaser": ObjectId(tenant),
            "project": ObjectId(projectid),
            "limit":datetime.datetime.strptime(limit, "%Y-%m-%d"),
            "remark": "",
            "createdAt": datetime.datetime.now(),
            "updatedAt": datetime.datetime.now(),
            "delete": False
        }
        result = purchaseAdd(data)
        print(result)
    except:
        print('参数错误')

