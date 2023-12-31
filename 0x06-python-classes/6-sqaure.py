#!/usr/bin/python3
"""Define a Square class for task 6"""


class Square:
    """class with private instance attribute"""
    def __init__(self, size=0, position=(0, 0)):
        """initialize  a new Square

        Args:
            size (int): size of the new Square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """set the current size of the square"""

        return(self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """the current position is set"""

        return(self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Method to that returns the area based on the size"""
        return (self.__size ** 2)

    def my_print(self):
        """Method that prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
