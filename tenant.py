# -*- coding:utf-8 -*-
import requests
import config
import time


class Tenant:
    def __init__(self, obj):
        '''
        :param obj:  {'name':'租户名称','namespace':'租户名空间','remark':'租户的简介描述'}
        '''
        self.name = obj['name']
        self.namespace = obj['namespace']
        self.remark = obj['remark']

    def createTenant(self):
        tenant_json = {
            "activated": True,
            "logo": None,
            "name": self.name,
            "namespace": self.namespace,
            "remark": self.remark,
            "resources": {
                "templates": {
                    "pod": {
                        "apiVersion": "v1",
                        "kind": "Pod",
                        "metadata": {
                            "name": "job-{}-{}"
                        },
                        "spec": {
                            "containers": [
                                {
                                    "args": [
                                        "/bin/sh",
                                        "-c",
                                        "{}"
                                    ],
                                    "image": "registry.orientsoft.cn/gitbox/alpine-git:lastest",
                                    "imagePullPolicy": "IfNotPresent",
                                    "name": "copy",
                                    "volumeMounts": []
                                }
                            ],
                            "restartPolicy": "Never",
                            "ttlSecondsAfterFinished": 0,
                            "volumes": []
                        }
                    },
                    "pv": {
                        "apiVersion": "v1",
                        "kind": "PersistentVolume",
                        "metadata": {
                            "name": "pv-{}-{}-{}",
                            "namespace": "{}",
                            "labels": {
                                "pv": "pv-{}-{}-{}"
                            }
                        },
                        "spec": {
                            "accessModes": ["ReadWriteMany"],
                            "capacity": {
                                "storage": "100Mi"
                            },
                            "nfs": {
                                "server": "{}",
                                "path": "{}{}"
                            }
                        }
                    },
                    "match_pvc": {
                        "apiVersion": "v1",
                        "kind": "PersistentVolumeClaim",
                        "metadata": {
                            "name": "pvc-{}-{}-{}",
                            "namespace": "{}"
                        },
                        "spec": {
                            "accessModes": [
                                "ReadWriteMany"
                            ],
                            "resources": {
                                "requests": {
                                    "storage": "100Mi"
                                }
                            },
                            "selector": {
                                "matchLabels": {
                                    "pv": "pv-{}-{}-{}"
                                }
                            },
                            "storageClassName": ""
                        }
                    },
                    "pvc": {
                        "apiVersion": "v1",
                        "kind": "PersistentVolumeClaim",
                        "metadata": {
                            "name": "pvc-{}-{}-{}",
                            "namespace": "{}"
                        },
                        "spec": {
                            "accessModes": ["ReadWriteMany"],
                            "storageClassName": "standard",
                            "resources": {
                                "requests": {
                                    "storage": "100Mi"
                                }
                            }
                        }
                    }
                }
            }
        }
        resp = requests.post(config.MOOP_TENANT_SERVICE_URL, json=tenant_json)
        if resp.status_code == 200:
            result = resp.json()
            print('创建租户成功，租户编号为：', result['id'])
            self.tenant = result['id']
        else:
            print('创建租户失败，原因：', resp.text)
            raise

    def deleteTenant(self):
        try:
            requests.delete(config.MOOP_TENANT_SERVICE_URL + '/' + self.tenant)
        except:
            pass

    def deleteVoume(self):
        try:
            payload = {
                'tenant': self.tenant,
                'username': "super",
                'tag': self.namespace
            }
            requests.delete(config.MOOP_VOLUME_SERVICE_URL + '/pvcs', params=payload)
            requests.delete(config.MOOP_VOLUME_SERVICE_URL + '/pvs', params=payload)
        except:
            pass

    def addPV(self):
        pv_json = {
            "tenant": self.tenant,
            "username": "super",
            "tag": self.namespace,
            "path": self.namespace
        }
        payload = {
            'tenant': self.tenant,
            'username': "super",
            'tag': self.namespace
        }
        # 创建pv
        requests.post(config.MOOP_VOLUME_SERVICE_URL + '/pvs', json=pv_json)
        # 查询pv状态
        while True:
            resp = requests.get(config.MOOP_VOLUME_SERVICE_URL + '/pvs', params=payload)
            if resp.status_code == 200:
                result = resp.json()
                if result['status']['phase'] != 'Pending':
                    print('PV创建成功')
                    break
                print('PV创建进度：', result['status']['phase'])
                time.sleep(1)
            else:
                print('PV创建失败原因：', resp.text)
                raise

    def addPVC(self):
        pvc_json = {
            "tenant": self.tenant,
            "username": "super",
            "tag": self.namespace,
            "match": True
        }
        payload = {
            'tenant': self.tenant,
            'username': "super",
            'tag': self.namespace
        }
        # 创建pvc
        requests.post(config.MOOP_VOLUME_SERVICE_URL + '/pvcs', json=pvc_json)
        # 查询pvc状态
        while True:
            resp = requests.get(config.MOOP_VOLUME_SERVICE_URL + '/pvcs', params=payload)
            if resp.status_code == 200:
                result = resp.json()
                if result['status']['phase'] != 'Pending':
                    print('PVC创建成功')
                    break
                print('PVC创建进度：', result['status']['phase'])
                time.sleep(1)
            else:
                print('PVC创建失败原因：', resp.text)
                raise

