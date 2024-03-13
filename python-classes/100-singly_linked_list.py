#!/usr/bin/python3
"""
Defines Node
"""


class Node:
    """Node  class defined by data"""

    @property
    def data(self):
        """retrieving data"""
        return self.__data

    @data.setter
    def data(self, value):
        """sets the value of data, value must be an integer"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        
        self.__data = value

        @property
        def next_node(self):
            """retrieving data"""
            return self.__next_node

        @next_node.setter
        def next_node(self, value):
            if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

        def __init__(self, data, next_node=None):
            """instantiation data and self node"""
            self.__data=data
            self.__next_node=next_node

class SinglyLinkedList:
    """define class SinglyLinkedList"""

    def __init__(self):
        self.__head=None
