class Person(object):
    """
    判断两个对象是否相等,重写__hash__和__eq__方法即可
    """
    def __init__(self, uid):
        self.uid = uid

    def __repr__(self):
        return 'Person(%s)' % self.uid

    def __hash__(self):
        return self.uid

    def __eq__(self, other):
        return self.uid == other.uid


p1 = Person(1)
p2 = Person(1)
p3 = Person(2)
print(p1 == p2)
print(set([p1, p2, p3]))