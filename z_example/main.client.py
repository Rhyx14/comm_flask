import sys
sys.path.append('..')
import numpy as np
from comm_flask.client import call_blob,call
import cv2
from comm_flask.utils.timespan import Timespan
import requests
window=cv2.namedWindow('asdf')
s= requests.Session()
while(1):
    with Timespan('call'):
        param,blob=call_blob('127.0.0.1:14370','get_picture')
    with Timespan('decode'):
        frame=np.fromstring(blob,np.uint8)
        frame=cv2.imdecode(frame,cv2.IMREAD_COLOR)
        cv2.imshow('asdf',frame)
        cv2.waitKey(1)

    # 普通call
    # _=call('127.0.0.1:14370','test','{}')

