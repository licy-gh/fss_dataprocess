# -*- coding:utf-8 -*-
import json
import sys
import os
import numpy as np
import pandas as pd
from obs import *
from dp_metrics import *

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

def image_thumbnail(fileName):
    print("*********filename:" + fileName)
    fileNamePath = TEMP_ROOT_PATH + fileName
    im = Image.open(fileNamePath)
    print("*********open image success******")
    w, h = im.size
    im.thumbnail((w//2, h//2))

    name = fileName.split('.')
    outFileName = name[0] + '-thumbnail.' + name[1]
    outFilePath = TEMP_ROOT_PATH + outFileName

    if im:
        im.save(outFilePath)

    else:
        print("Sorry, Failed.")

    return outFileName, outFilePath

def handler (event, context):
    srcBucket, srcObjName = getObjInfoFromObsEvent(event)
    obs_address = context.getUserData('obs_address')
    outputBucket = context.getUserData('obs_output_bucket')
    if (obs_address is None) or (outputBucket is None):
        print("*** obs_address or outputBucket is None")
        return 'False'

    print("*** srcBucketName: {}".format(srcBucket))
    print("*** srcObjName: {}".format(srcObjName))
    print("*** obs_address: {}".format(obs_address))
    print("*** output bucket: {}".format(outputBucket))

    client = newObsClient(context, obs_address)
    # download file uploaded by user from obs
    localFile = TEMP_ROOT_PATH + srcObjName
    downloadFile(client, srcBucket, srcObjName, localFile)

    outFile, outputFileName = image_thumbnail(srcObjName)

    # 将转换后的文件上传到新的obs桶中
    uploadFileToObs(client, outputBucket, outFile, outputFileName)
    return 'OK'

