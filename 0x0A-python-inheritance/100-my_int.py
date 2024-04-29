#!/usr/bin/python3
"""
=============================
Module with a class Myint
=============================
"""


class MyInt(int):
    """class that inherits from int"""

    def __init__(self, my_int):
        self.my_int = my_int

    @property

    def my_int(self):
        return self.__my_int

    @my_int.setter

    def my_int(self, value):

        if type(value) is not int:
            raise TypeError ("my_int must be an integer")
        else:
            self.__my_int = value

    def __eq__(self, newVal):
        """the equal method"""

        if self.my_int == newVal:
            return False
        else:
            return True
    
    def __ne__(self, newVal):
        """not equal method"""

        if self.my_int != newVal:
            return False
        else:
            return True

my_i = MyInt(3)
print(my_i)
print(my_i == 3)
print(my_i != 3)
