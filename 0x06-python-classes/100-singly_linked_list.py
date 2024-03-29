#!/usr/bin/python3
"""Define a SinglyLinkedList class and the Node"""


class Node:
    """Node class"""

    def __init__(self, data, next_node=None):
        """Initialize a new Node.
        :param data: The data of the Node
        :param next_node: The next Node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """getter and setter of data of the Node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """getter and setter of data of the Node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """SinglyLinkedList class"""

    def __init__(self):
        """Initialize a new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """
        Insert a new Node into the correct sorted position
        in the list.
        :param value: The value to be inserted
        """

        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Return the string representation of the list."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
