#!/usr/bin/python3
"""A singly linked list"""


class Node:
    """A class called Node with private instance\
    attribute 'data' & 'next_node'"""
    def __init__(self, data, next_node=None):
        """Instantiate with data and next_node attributes"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """To retrieve data """
        return self.__data

    @data.setter
    def data(self, value):
        """To set the data"""
        if type(value) is not int:
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """To retrieve the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """To set the value of the next node"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """A class called singly linked list with\
    private instance attribute head"""

    def __init__(self):
        """Initialize"""
        self.head = None

    def __str__(self):
        """To read and print out all the members of\
        the singlylinkedlist class"""
        new_str = ''
        node = self.head
        while node:
            new_str += str(node.data)
            new_str += '\n'
            node = node.next_node
        return new_str[:-1]

    def sorted_insert(self, value):
        """Adds a new Node to the sorted linked list."""
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return
        if value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        node = self.head
        while node.next_node and node.next_node.data < value:
            node = node.next_node
        new_node.next_node = node.next_node
        node.next_node = new_node
