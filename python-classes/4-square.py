#!/usr/bin/python3
"""
defines Square
"""


class Square:
    """Square class defined by size"""

    @property
     def size(self):
        """retrieving size"""
        
        return self.__size

    @size.setter
    def size(self, value):
        """ sets the value of size , value must be integer"""

    if type(size) is not int:
         raise TypeError("size must be an integer")
     if size < 0:
         raise ValueError("size must be >= 0")

     self.__size = size

     def __init__(self, size=0):
         """Instantiation with optional"""
         self.size= size

     def area(self):
         """ calculate and return the current square area."""
         return self.__size ** 2


