#!/usr/bin/env python
# coding=utf-8

from qcloud_cos import CosClient
from qcloud_cos import UploadFileRequest

appid = 100000    # 替换为你的appid
secret_id = u''   # 替换为你的secret_id
secret_key = u''  # 替换为你的secret_key
bucket = u''      # 替换为你要操作的bucket名
region = "tj"     # 替换为该bucket所属的地区代码, tj/sh/gz/sgp
cos_client = CosClient(appid, secret_id, secret_key, region)

##################################
# 文件操作                        #
##################################
# 上传文件(默认不允许覆盖)
# 将本地的 upload_example.txt 上传到 bucket 的根分区下,并命名为 upload_sample_python.txt

request = UploadFileRequest(bucket, u'/upload_sample_python.txt', u'/data/upload/upload_example.txt')
upload_file_response = cos_client.upload_file(request)

print upload_file_response
