"""
__setattr__ : 属性赋值
__getattr__ : 获取属性, ⚠️: 只有在访问不存在的属性时,此方法才会被调用
__getattribute__ : 所以任意的属性+方法都经过这里
__delattr__: 属性删除
"""