# coding: utf-8


class Node(object):
    """
    data: 节点保存的数据
    _next:保存下一个节点对象
    """

    def __init__(self, data):
        self.data = data
        self._next = None

    def __repr__(self):
        """
        用来定义Node的字符输出
        Returns:
            字符串输出
        """
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def append(self, data):
        """"
        在链表末尾添加node值，如果是node对象直接添加，否则先转换为node对象
        Args:
            data：数据或者node对象
        Returns:
            None
        """
        if isinstance(data, Node):
            item = data
        else:
            item = Node(data)
        if not self.head:
            self.head = item
        else:
            node = self.head
            while node._next:
                node = node._next
            node._next = item
        self.length += 1

    def delete(self, index):
        """
        删除链表中某个位置的节点
        Args:
            index: 位置索引
        Returns:
            None
        """
        if isinstance(index, int):
            if index > self.length:
                print("index is out of range")
                return
            else:
                if index == 0:
                    self.head = self.head._next
                else:
                    current_node = self.head
                    while index - 1:
                        current_node = current_node._next
                        index -= 1
                    current_node._next = current_node._next._next
                self.length -= 1
                return
        else:
            print("index value is not int")
            return

    def insert(self, index, value):
        """
        链表的插入操作
        Args:
            value: 要插入的值
            index: 位置索引
        Returns:
            None
        """
        if isinstance(index, int):
            if index > self.length:
                print("index is out of range")
                return
            else:
                this_node = Node(data=value)
                current_node = self.head

                if index == 0:
                    self.head = this_node
                    this_node._next = current_node
                    return
                while index - 1:
                    current_node = current_node._next
                    index -= 1
                this_node._next = current_node._next
                current_node._next = this_node
                self.length += 1
                return
        else:
            print("index value is not int")
            return

    def update(self, index, value):
        """
        为链表中某个位置的节点修改值
        Args:
            value: 要修改的值
            ndex: 位置索引
        Returns:
            None
        """
        if isinstance(index, int):
            if index > self.length:
                print("index is out of range")
                return
            else:
                this_node = Node(data=value)

                if index == 0:
                    this_node._next = self.head
                    self.head = this_node
                else:
                    current_node = self.head
                    while index - 1:
                        current_node = current_node._next
                        index -= 1
                    this_node._next = current_node._next._next
                    current_node._next = this_node
        else:
            print("index value is not int")
            return

    def get_value(self, index):
        """
        获取链表中某个位置节点的值
        Args:
            index: 位置索引
        Returns:
             该节点值
        """
        if isinstance(index, int):
            if index > self.length:
                print("index is out of range")
                return
            else:
                if index == 0:
                    return self.head.data
                else:
                    current_node = self.head
                    while index - 1:
                        current_node = current_node._next
                        index -= 1
                    return current_node._next.data
        else:
            print("index is not int")
            return

    def clear(self):
        """
        清空链表
        """
        self.head = None
        self.length = 0
        print("clear the linkedlist finished")

    def print_linked_list(self):
        """
        对整个链表打印
        """
        if self.is_empty():
            print("linked list length is 0")
        else:
            node = self.head
            print("Head -->", node.data, end=" ")
            while node._next:
                node = node._next
                print("-->", node.data, end=" ")
            print("--> None, Linked list finish")


if __name__ == '__main__':
    n1 = Node(data="node1")
    n2 = Node(data="node2")
    l = LinkedList()
    l.append(n1)
    l.append(n2)
    l.print_linked_list()
    l.insert(1, "mao")
    l.print_linked_list()
    l.update(index=2, value="chong")
    l.print_linked_list()
    print(l.get_value(index=2))
    print(l.length)
