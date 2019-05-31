# -*- coding:utf-8 -*-
import os
# 程序的mongo地址
MONGODB_URI = 'mongodb://{}:{}'.format(os.environ['MONGODB_IP'],os.environ['MONGODB_PORT'])
SERVER_MONGODB_NAME = 'MOOP'
SERVICE_MONGODB_NAME = 'MOOP_SERVICE'
# 租户service的地址
MOOP_TENANT_SERVICE_URL = 'http://{}:{}/service/v1/tenants'.format(os.environ['TENANT_SERVICE_IP'],os.environ['TENANT_SERVICE_PORT'])
# project service的地址
MOOP_PROJECT_SERVICE_URL = 'http://{}:{}/service/v1'.format(os.environ['PROJECT_SERVICE_IP'],os.environ['PROJECT_SERVICE_PORT'])
# volume service的地址
MOOP_VOLUME_SERVICE_URL = 'http://{}:{}/service/v1/volumes'.format(os.environ['VOLUME_SERVICE_IP'],os.environ['VOLUME_SERVICE_PORT'])
