#!/usr/bin/python3
"""
Defines a Square
"""


class Square:
    """Square class defined by size"""
    
    def __init__(self, size=0):
        """ Instantiation with optional  """

        if type(size) is not int :
            raise TypeError ("size must be an integer")
        if size < 0:
            raise ValueError (" size must be >= 0")

        self.__size=size 

