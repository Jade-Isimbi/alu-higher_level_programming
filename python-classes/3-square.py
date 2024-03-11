
class Square:
    """Square class defined by size"""

    def __init__(self, size=0):
        """Instantiation with optional size"""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Public instance method to calculate and return the current square area."""
        return self.__size ** 2