import time
class Timespan():
    def __init__(self,name='') -> None:
        self._name=name
        pass

    def __enter__(self,*args,**kwargs):
        self._time=time.time()
    
    def __exit__(self,*args,**kwargs):
        print(f"执行{self._name}时间为:{time.time()-self._time}")