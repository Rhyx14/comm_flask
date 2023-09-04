import json
import requests
from .protobuf.msg_pb2 import msg_pb2

def call(host,func:str,param:dict):
    x = requests.post(f'http://{host}/call',json={'func_name':func,'param':param})
    js= json.loads(x.text)
    return js['ret']

def call_blob(host,func:str,param:str,blob:bytes=b''):
    a=msg_pb2.MsgRequest()
    a.method_name=func
    a.params=param
    a.blob=blob

    x=requests.post(f'http://{host}/call_blob',
        data=a.SerializeToString(),
        headers={'Content-Type':'application/octet-stream'})

    b=msg_pb2.MsgResponse()
    b.ParseFromString(x.content)
    return b.returns,b.blob
# print(call('127.0.0.1:5000','a',{"name":1}))
# x= requests.get('http://www.baidu.com/')