# coding: utf-8


class Node(object):
    """
    data: 节点保存的数据
    _next:保存下一个节点对象
    """

    def ___init__(self, data, pnext=None):
        self.data = data
        self._next = pnext

    def __repr__(self):
        """
        用来定义Node的字符输出
        print为输出data
        """
        return str(self.data)

    def __getitem__(self, index):
        pass

    def __setitem__(self, ind, val):
        pass

    def __len__(self):
        return self.length

    def is_empty(self):
        return (self.length == 0)

    def append(self, data):
        pass

    def delete(self, index):
        pass

    def insert(self, index, data_or_node):
        pass

    def update(self, index, data):
        pass

    def get_item(self, index):
        pass

    def get_index(self, data):
        pass

    def clear(self):
        pass
