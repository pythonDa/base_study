class Person(object):
    """
    __new__:参数为cls,有返回且为实例对象,所以可以对实例进行统一的初始化操作
    __init__:参数为self，无返回值，只是初始化操作
    使用场景:
      __new__ 返回优先于__init__,且返回实例,可以使用此方法实现单例类
    """

    def __new__(cls, *args, **kwargs):
        print('call __new__')
        return object.__new__(cls)

    def __init__(self, name, age):
        print('call __init__')
        self.name = name
        self.age = age


class Singleton(object):
    """
    单例模式
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class g(float):
    """
    继承内置类 int, str, tuple
    千克转克
    """
    def __new__(cls, kg):
        return float.__new__(cls, kg*1000)


if __name__ == '__main__':
    # p = Person('zhangsan', 20)
    # for _ in range(1000):
    #     a = Singleton()
    #     print(a)
    a = g(50)
    print(a+1000)
