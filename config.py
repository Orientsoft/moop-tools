SESSION_TYPE = 'mongodb'  # session的mongo地址
SESSION_MONGODB = 'mongodb://192.168.0.48:38213'
# session的db名称
SESSION_MONGODB_DB = 'MOOP_SERVICE'
# session的collection名称
SESSION_MONGODB_COLLECT = 'sessions'
# session的前缀
SESSION_KEY_PREFIX = 'session'
# session超时时间
# 加密key
SECRET_KEY = 'abcdefg'
# 程序的mongo地址
MONGODB_URL = 'mongodb://192.168.0.31:32017/MOOP'
# 日志格式
LOG_FORMAT = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s:%(funcName)s - [%(levelname)s] %(message)s'
# 租户service的地址
MOOP_TENANT_SERVICE_URL = 'http://192.168.0.48:7778/service/v1'
# project service的地址
MOOP_PROJECT_SERVICE_URL = 'http://192.168.0.48:7779/service/v1'
# volume service的地址
MOOP_VOLUME_SERVICE_URL = 'http://192.168.0.48:5010/service/v1/volumes'
# pod service的地址
MOOP_POD_SERVICE_URL = 'http://192.168.0.48:5020/service/v1'
# launcher service的地址
MOOP_LAUNCHER_SERVICE_URL = 'http://192.168.0.31:30264/services/launcher'
# sms service的地址
SMS_SERVICE_URL = 'http://192.168.0.31:31785/api/v1'
# es service的地址
AUDIT_SERVICE_URL = 'http://192.168.0.31:31786'
# report service的地址
REPORT_SERVICE_URL = 'http://192.168.0.31:31787/api/v1'
# matplot service的地址
MATPLOT_SERVICE_URL = 'http://192.168.0.31:31788/api/v1'
