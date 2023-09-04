from flask import Flask,request,jsonify,Response
import json
import logging
from .protobuf.msg_pb2 import msg_pb2
FlaskApp= Flask(__name__)

logger=logging.getLogger('comm_flask')

function_dict={}
def rpc_method(func):
    '''
    添加相应函数,

    func : callable(**param)

    param 为参数
    '''
    function_dict[func.__name__]=func
    return func

blob_function_dict={}
def rpc_blob_method(func):
    '''
    添加函数,传输blob对象
    '''
    blob_function_dict[func.__name__]=func
    return func

@FlaskApp.route('/')
def hello_world():
    # TODO 显示function_list
    return str(function_dict+blob_function_dict)

@FlaskApp.route('/call_blob',methods=['POST'])
def on_call_blob():
    '''
    protobuf version
    '''
    rslt=msg_pb2.MsgResponse()
    rslt.returns='-1'

    try:
        text=request.data
        pb=msg_pb2.MsgRequest()
        pb.ParseFromString(text)
        rslt.returns,rslt.blob=blob_function_dict[pb.method_name](pb)        
    except KeyError:
        logger.error(f'no such method {pb.method_name}')
        
    return Response(rslt.SerializeToString(),content_type='application/octet-stream')

@FlaskApp.route('/call',methods= ['POST'])
def on_call():
    '''
    json版
    '''
    rslt={'ret':-1}
    if(request.method == 'POST'):
        try:
            js=json.loads(request.get_data(as_text=True))
            name=js['func_name']
            rslt['ret']=function_dict[name](**js['param'])        
        except KeyError:
            logger.error(f'no such method {name}')
        except TypeError:
            logger.error(f'{name}() got unexpected keyword arguments {js["param"]}')

    return jsonify(rslt)

def start_async(host='localhost',port=14370):
    import threading
    threading.Thread(target=start,args=(host,port)).start()

def start(host='localhost',port=14370):
    FlaskApp.run(host,port)
if __name__ == '__main__':
    FlaskApp.run()