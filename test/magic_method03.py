"""
类:
__str__: 强调可读性,目标是用户  %s __str__
__repr__: 强调准确性/标准性,目标是机器,返回值是可执行的, eval可   %r __repr__
__unicode__   目前好像不再使用
__hash__/__eq__
__nonzero__  目前好像不再使用
"""
import datetime
b = datetime.datetime.now()
print(str(b))
print('%s' % b)
print(repr(b))
print('%r' % b)


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return 'name: %s, age: %s' % (self.name, self.age)

    def __repr__(self):
        return 'Person("%s", %s)' % (self.name, self.age)


person = Person('zhangsan', 20)
print('%s' % person)
print(str(person))
print('%r' % person)  # 机器可执行
print(repr(person))


