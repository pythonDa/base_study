"""
构造与初始化
__init__
__new__
__del__
"""
class Person(object):
    """
    析构方法,对象被垃圾回收时调用
    python是通过引用计数来进行垃圾回收的
    """
    def __del__(self):
        print('__del__')


if __name__ == '__main__':
    p = Person()
    b = p
    del p
    print('exit')
