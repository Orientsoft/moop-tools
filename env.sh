#!/bin/bash
db_name_space="database"
share_namespace="moop-share-services"
private_namespace="moop-lab" #按需要修改

export SERVER_MONGODB_NAME='MOOP'
export SERVICE_MONGODB_NAME='MOOP_SERVICE'
export TENANTNAME='Orient'  #按需修改
export TENANTREMARK='测试租户的简介描述'  #按需修改

export NAMESPACE=$private_namespace

export MONGODB_IP=$(kubectl get svc --namespace $db_name_space mongodb -o jsonpath='{.spec.clusterIP}')
export MONGODB_PORT=$(kubectl get svc --namespace $db_name_space mongodb -o jsonpath='{.spec.ports[0].port}')

export TENANT_SERVICE_IP=$(kubectl get svc --namespace $share_namespace tenant-service -o jsonpath='{.spec.clusterIP}')
export TENANT_SERVICE_PORT=$(kubectl get svc --namespace $share_namespace tenant-service -o jsonpath='{.spec.ports[0].port}')

export PROJECT_SERVICE_IP=$(kubectl get svc --namespace $share_namespace project-service -o jsonpath='{.spec.clusterIP}')
export PROJECT_SERVICE_PORT=$(kubectl get svc --namespace $share_namespace project-service -o jsonpath='{.spec.ports[0].port}')

export VOLUME_SERVICE_IP=$(kubectl get svc --namespace $private_namespace volume-service -o jsonpath='{.spec.clusterIP}')
export VOLUME_SERVICE_PORT=$(kubectl get svc --namespace $private_namespace volume-service -o jsonpath='{.spec.ports[0].port}')