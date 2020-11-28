"""
比较操作:
__cmp__ python3好像不支持此方法
__eq__
__ne__
__lt__
__gt__
"""
from filecmp import cmp


class Person01(object):
    """
    __cmp__ 比较
    """
    def __init__(self, uid):
        self.uid = uid

    def __cmp__(self, other):
        if self.uid == other.uid:
            return 0
        elif self.uid > other.uid:
            return 1
        return -1

    def __eq__(self, other):
        return self.uid == other.uid

    def __gt__(self, other):
        return self.uid > other.uid

    def __lt__(self, other):
        return self.uid < other.uid


if __name__ == '__main__':
    p1 = Person01(1)
    p2 = Person01(2)
    # c = p1 > p2
    # print(c)
    print(p1 > p2)