"""
容器类操作
__setitem__
__getitem__
__delitem__
__len__
__iter__
__contains__
__reversed__
"""


class MyList(object):
    def __init__(self, values=None):
        self.values = values or []

    def __setitem__(self, key, value):
        self.values[key] = value

    def __getitem__(self, key):
        return self.values[key]

    def __delitem__(self, key):
        del self.values[key]

    def __len__(self):
        return len(self.values)

    def __iter__(self):
        return self

    def __contains__(self, key):
        return key in self.values

    def __reversed__(self):
        return list(reversed(self.values))


if __name__ == '__main__':
    mylist = MyList([1,2,3,4,5])
    print(mylist[0])