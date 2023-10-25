#!/usr/bin/python3
"""Define a Square class or task 3"""


class Square:
    """class with instance attribute of private"""
    def __init__(self, size=0):
        """initialize  a new Square

        Args:
            size (int): size of the new Square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Method to that returns the area based on the size"""
        return (self.__size ** 2)
