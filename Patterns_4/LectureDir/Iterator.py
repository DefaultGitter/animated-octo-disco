class MyIterator:
    def __init__(self, collection):
        self.collection = collection
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.collection):
            item = self.collection[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration()


class MyCollection:
    def __init__(self):
        self.items = []

    def add(self, _item):
        self.items.append(_item)

    def __iter__(self):
        return MyIterator(self.items)
        # return iter(self.items)


mc = MyCollection()
mc.add('a1')
mc.add('a2')
mc.add('a3')
mc.add('a4')

for item in mc:
    print(item)
