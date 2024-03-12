#!/usr/bin/python3
"""
Defines Square
"""


class Square:
    """Square class defined by size"""

    @property
    def size(self):
        """retrieving size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the value of size, value must be an integer"""
        if type (value) is not int:
            raise TypeError("size must be an integer")
        if size<0 :
            raise ValueError ("size must be >= 0")

        self.__size = value

     def __init__(self, size=0):
        """Instantiation with optional size"""
        self.size = size

    def area(self):
        """calculate and return the current square area."""
        return self.__size ** 2

    def my_print(self):
        if self.__size==0 :
            print ("")
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        
        

