# -*- coding:utf-8 -*-
from pymongo import MongoClient
import config
from bson import ObjectId
import datetime
import requests

connect = MongoClient(config.MONGODB_URI)
servicedb = connect[config.SERVICE_MONGODB_NAME]
serverdb = connect[config.SERVER_MONGODB_NAME]


# connect = MongoClient('mongodb://192.168.0.31:32017')
# servicedb = connect['MOOP_SERVICE']
# serverdb = connect['MOOP']

def get_projects(List=None, embed=None):
    List = [str(x) for x in List]
    result = {}
    import urllib
    payload = {
        'id': List,
        'embed': 1
    }
    r = requests.get('http://192.168.0.34:32280/services/v1/project/projects', params=urllib.parse.urlencode(payload),
                     headers={'moopkey': 'faf23ej21fklajfla'})
    if r.status_code == 200:
        result = r.json()
    return result

def getClassroom():
    classroom = serverdb.classroom.find({"delete": False})
    for c in classroom:
        cid = c['_id']
        projects = get_projects(c['projects'])
        gits = []
        for key, value in projects.items():
            gits.append('git clone {}'.format(value['spec']))
        cmd = 'cd /opt/minio-root/moop-lab/{cid} && mkdir data && mv * data/;mkdir projects && cd projects && {gitcmd} '.format(cid=cid,gitcmd=' && '.join(gits))
        print(cmd)



if __name__ == '__main__':
    getClassroom()
