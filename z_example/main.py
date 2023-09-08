import sys
sys.path.append('..')
import numpy as np
from comm_flask.server import rpc_blob_method,rpc_method,start
import cv2
from comm_flask.utils.timespan import Timespan

cap=cv2.VideoCapture(0)
cap.set(3,512)
cap.set(4,512)
@rpc_blob_method
def get_picture(pd):
    # with Timespan('cap'):
    ret,frame=cap.read()
    # with Timespan('encode'):
    _,frame=cv2.imencode('.png',frame)
    frame=np.array(frame)
    return 'png', frame.tostring()

@rpc_method
def test():
    return 0

start('127.0.0.1')

