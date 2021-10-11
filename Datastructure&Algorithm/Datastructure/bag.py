class Bag(object):

    def __init__(self, maxsize=10):
        self.maxsize = maxsize
        self._items = list()

    def add(self, other):
        if len(self._items) > self.maxsize:
            raise Exception('Bag is full.')

        self._items.append(other)

    def remove(self, item):
        self._items.remove(item)

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        for _item in self._items:
            yield _item


def test_bag():
    bag = Bag()

    bag.add(1)
    bag.add(2)
    bag.add(3)
    assert len(bag) == 3

    bag.remove(2)
    assert len(bag) == 2

    for item in bag:
        print(item)
