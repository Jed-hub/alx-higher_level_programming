#!/usr/bin/python3
"""
Module my list with one class
and one method
"""

class MyList(list):
    """
    This class contains one function

    Initialization
    """
    def print_sorted(self):
        """
        This method prints the list
        sorted (ascending sort)
        """
        my_list = []
        for element in self:
            if type(element) is int:
                my_list.append(element)
        my_list.sort()

        print(my_list)
