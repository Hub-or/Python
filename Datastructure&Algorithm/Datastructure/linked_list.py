class Node(object):
    """链表中的单个节点类"""
    def __init__(self, value=None, next=None):
        self.value, self.next = value, next


class LinkedList(object):
    """链表ADT主体类"""
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self.root = Node()
        self.length = 0

    def __len__(self):
        return self.length

