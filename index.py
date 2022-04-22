# -*- coding:utf-8 -*-
import importlib
import json
import os
import sys
from obs import *

current_file_path = os.path.dirname(os.path.realpath(__file__))
# append current path to search paths, so that we can import some third party libraries.
sys.path.append(current_file_path)

METRICS_PATH = os.environ.get('RUNTIME_CODE_ROOT') + '/dp_metrics/'
TEMP_ROOT_PATH = "/tmp/"
secure = True
signature = 'v4'
port = 443
path_style = True

def newObsClient(context, obs_server):
    ak = context.getAccessKey()
    sk = context.getSecretKey()
    return ObsClient(access_key_id=ak, secret_access_key=sk, server=obs_server,
                     path_style=True, ssl_verify=False, max_retry_count=5, timeout=20)

def downloadFile(obsClient, bucket, objName, localFile):
    resp = obsClient.getObject(bucket, objName, localFile)
    if resp.status < 300:
        print('download file ', objName, 'succeed')
    else:
        print('download failed, errorCode: {}, errorMessage: {}, requestId: {}'.format(resp.errorCode, resp.errorMessage,
              resp.requestId))

def uploadFileToObs(client, bucket, objName, file):
    resp = client.putFile(bucket, objName, file)
    if resp.status < 300:
        print('upload file ', file, 'succeed')
    else:
        print('upload failed, errorCode: {}, errorMessage: {}, requestId: {}'.format(resp.errorCode, resp.errorMessage,
              resp.requestId))

def getObjInfoFromObsEvent(event):
    if 's3' in event['Records'][0]:
        s3 = event['Records'][0]['s3']
        eventName = event['Records'][0]['eventName']
        bucket = s3['bucket']['name']
        objName = s3['object']['key']
    else:
        obsInfo = event['Records'][0]['obs']
        eventName = event['Records'][0]['eventName']
        bucket = obsInfo['bucket']['name']
        objName = obsInfo['object']['key']
    print("*** obsEventName: {}, srcBucketName: {}, objName: {}".format(eventName, bucket, objName))
    return bucket, objName


def PostObject(obsAddr, bucket, objName, ak, sk):
    TestObs = ObsClient(access_key_id=ak, secret_access_key=sk,
                        is_secure=secure, server=obsAddr, signature=signature, path_style=path_style,ssl_verify=False, port=port,
                        max_retry_count=5, timeout=20)


    Lheaders = PutObjectHeader(md5=None, acl='private', location=None, contentType='text/plain')

    Lheaders.sseHeader = SseKmsHeader.getInstance()
    h = PutObjectHeader()
    Lmetadata = {'key': 'value'}

    objPath = TEMP_ROOT_PATH + objName
    resp = TestObs.postObject(bucketName=bucket, objectKey=objName, file_path=objPath,
                              metadata=Lmetadata, headers=h)
    if isinstance(resp, list):
        for k, v in resp:
            print('PostObject, objectKey',k, 'common msg:status:', v.status, ',errorCode:', v.errorCode, ',errorMessage:', v.errorMessage)
    else:
        print('PostObject, common msg: status:', resp.status, ',errorCode:', resp.errorCode, ',errorMessage:', resp.errorMessage)


def handler (event, context):
    srcBucket, srcObjName = getObjInfoFromObsEvent(event)
    obs_address = context.getUserData('obs_address')
    outputBucket = context.getUserData('obs_output_bucket')
    if (obs_address is None) or (outputBucket is None):
        print("*** obs_address or outputBucket is None")

    print("*** srcBucketName: {}".format(srcBucket))
    print("*** srcObjName: {}".format(srcObjName))
    print("*** obs_address: {}".format(obs_address))
    print("*** output bucket: {}".format(outputBucket))

    client = newObsClient(context, obs_address)
    # download file uploaded by user from obs
    localFile = TEMP_ROOT_PATH + srcObjName
    downloadFile(client, srcBucket, srcObjName, localFile)

    # 数据处理方法
    metrics_impl = [os.path.splitext(f)[0] for f in os.listdir(os.path.join(METRICS_PATH)) if f.endswith('.py')]
    raw_data = json.load(open(localFile)) # 读取下载下来的数据
    op = raw_data['operation'] # 获取操作

    if op in metrics_impl:
        dp_module = importlib.import_module('dp_metrics.' + op)
        if hasattr(dp_module, op):
            print('*** execute function {}'.format(op))
            res = {'res' : getattr(dp_module, op)(raw_data)}
        else:
            res = '*** operation not found'

    outFileName = srcObjName.split('.')[0] + op + '-res.json'
    outFilePath = TEMP_ROOT_PATH + outFileName

    json.dumps(res) # print输出
    with open(outFilePath, 'w') as saving_file: # 写入文件
        json.dump(res, saving_file)

    # 将转换后的文件上传到新的obs桶中
    uploadFileToObs(client, outputBucket, outFileName, outFilePath)
    return 'OK'