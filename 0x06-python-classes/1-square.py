#!/usr/bin/python3
""" Working on object oriented programming using  python """
class Square:
    def __init__(self, size=0):
        """Initialize a Square instance with a size.

        Args:
            size (int, optional): The size of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int) or size < 0:
            raise TypeError("size must be a non-negative integer")
        self.__size = size

if __name__ == "__main__":
    try:
        my_square_1 = Square(3)
        print(type(my_square_1), my_square_1.__dict__)

        my_square_2 = Square()
        print(type(my_square_2), my_square_2.__dict__)

        print(my_square_1.__size)  # Accessing private attribute
    except Exception as e:
        print(e)

    try:
        my_square_3 = Square("3")
        print(type(my_square_3), my_square_3.__dict__)
    except Exception as e:
        print(e)

    try:
        my_square_4 = Square(-89)
        print(type(my_square_4), my_square_4.__dict__)
    except Exception as e:
        print(e)

