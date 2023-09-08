import json
import requests
from .protobuf.generated import msg_pb2
from .utils.timespan import Timespan

def call(host,func:str,param:dict):
    x = requests.post(f'http://{host}/call',json={'func_name':func,'param':param})
    js= json.loads(x.text)
    return js['ret']

def call_blob(host,func:str,param:str='',blob:bytes=b'',session:requests.Session=None):

    a=msg_pb2.MsgRequest()
    a.method_name=func
    a.params=param
    a.blob=blob
    if session is not None:
        x=session.post(f'http://{host}/call_blob',
            data=a.SerializeToString(),
            headers={'Content-Type':'application/octet-stream'})
    else:    
        x=requests.post(f'http://{host}/call_blob',
            data=a.SerializeToString(),
            headers={'Content-Type':'application/octet-stream'})

    b=msg_pb2.MsgResponse()
    b.ParseFromString(x.content)
    return b.returns,b.blob