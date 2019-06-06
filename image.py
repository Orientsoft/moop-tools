# -*- coding:utf-8 -*-
from pymongo import MongoClient
import config
import docker

client = docker.from_env()

connect = MongoClient(config.MONGODB_URI)


# 创建image
def imageAdd(data):
    servicedb = connect[config.SERVICE_MONGODB_NAME]
    image = servicedb.image.find_one({'url': data['url']})
    if image:
        return '镜像已存在'
    print('=' * 30)
    print('开始拉取镜像...')
    # client.images.pull()
    pull_log = client.api.pull(data['url'], tag=data['tag'], stream=True)
    for x in pull_log:
        print(x)
    print('镜像拉取成功')
    servicedb.image.insert({
        'url': data['url']+data['tag'],
        'desc': data['desc'],
        'package': data['package'],
        'delete': False
    })
    return '创建成功'


if __name__ == '__main__':
    # 创建image
    data = {'url': 'registry.datadynamic.io/moop/jupyter-chinese','tag':"20190430",'desc': '根管治疗镜像', 'package': ['numpy']}
    result = imageAdd(data)
    print(result)
