class AttrsIterator:
    c = -1
    a = []
    def __init__(self, obj):
        self.obj = obj
        for i in self.obj.__dict__:
            self.a.append((i, self.obj.__dict__[i]))
    def __iter__(self):
        yield from self.a
    def __next__(self):
        self.c += 1
        if len(self.a)==self.c:
            raise StopIteration
        return self.a[self.c]
class Kemal:
    def __init__(self):
        self.family = 'cats'
        self.breed = 'british'
        self.master = 'Kemal'


kemal = Kemal()
attrs_iterator = AttrsIterator(kemal)

print(next(attrs_iterator))
print(next(attrs_iterator))
print(next(attrs_iterator))