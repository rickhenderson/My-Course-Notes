"""
-------------------------------------------------------
stack_array.py
Array version of the Stack ADT.
-------------------------------------------------------
Author:  Rick Henderson
ID:      93something
Email:   rhenderson@wlu.ca
__updated__ = "2016-05-19"
Note: It's really a list.
-------------------------------------------------------
"""
from copy import deepcopy


class Stack:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty stack. Data is stored in a list.
        Use: s = Stack()
        -------------------------------------------------------
        Postconditions:
            Initializes an empty stack.
        -------------------------------------------------------
        """
        self._values = []
        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the stack is empty.
        Use: b = s.is_empty()
        -------------------------------------------------------
        Postconditions:
            returns True if the stack is empty, False otherwise.
        -------------------------------------------------------
        """
        # Simplified check
        empty = False

        if len(self._values) == 0:
            empty = True

        return empty

    def push(self, value):
        """
        -------------------------------------------------------
        Pushes a copy of value onto stack.
        Use: s.push(value)
        -------------------------------------------------------
        Preconditions:
            value - a data element (?)
        Postconditions:
            a copy of value is added to the top of the stack.
        -------------------------------------------------------
        """
        self._values.append(deepcopy(value))
        return

    def pop(self):
        """
        -------------------------------------------------------
        Pops and returns the top of stack.
        Use: value = s.pop()
        -------------------------------------------------------
        Postconditions:
            returns
            value - the value at the top of the stack - the value is
                removed from the stack (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot pop from an empty stack"

        # Allowed to use the list method called pop()
        value = self._values.pop()
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the top of the stack.
        Use: value = s.peek()
        -------------------------------------------------------
        Postconditions:
            returns
            value - a copy of the value at the top of the stack -
                the value is not removed from the stack (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot peek at an empty stack"

        # Pop the top value from the stack.
        value = deepcopy(self._values[len(self._values) - 1])

        return value
