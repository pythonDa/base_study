class Person(object):
    def __init__(self, uid):
        self.uid = uid

    def __nonzero__(self):
        return self.uid > 10


p1 = Person(5)
p2 = Person(12)
print(bool(p1))
print(bool(p2))
