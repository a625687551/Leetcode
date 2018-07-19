# -*- coding: utf-8 -*-


# 直接实例化
class Singleton(object):
    def foo(self):
        pass


# singleton = Singleton()

# from * import singleton


# 装饰器来解决
def singleton(cls, *args, **kwargs):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, ** kwargs)
            return instances[cls]
        return _singleton()


@singleton
class A(object):
    a = 1

    def __init__(self, x=0):
        self.x = x

a1 = A(2)
a2 = A(3)


# 使用类类解决
import time
import threading


class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        time.sleep(1)

    @classmethod
    def instance(cls, *args, **kwargs):
        with Singleton._instance_lock:
            if not hasattr(Singleton, "_instance"):
                Singleton._instance = Singleton(*args, **kwargs)
        return Singleton._instance


def task(arg):
    obj = Singleton.instance()
    print(obj)
for i in range(10):
    t = threading.Thread(target=task, args=[i, ])
    t.start()
time.sleep(20)
obj = Singleton.instance()
print(obj)
