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
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """retrieving position (getter)"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets the value of position, must be a tuple of 2 positive integers"""
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def __init__(self, size=0, position=(0, 0)):
        """Instantiation with optional size and position"""
        self.size = size
        self.position = position

    def area(self):
        """calculate and return the current square area."""
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print("")
        for i in range(0, self.__position[1]):
            print("")
        for i in range(0, self.__size):
            for j in range(0, self.__position[0]):
                print(" ", end="")
            for k in range(0, self.__size):
                print("#", end="")
            print("")
