"""
This file contains the low level implementation of the stack.
"""

from .exceptions import StackOutOfBounds, StackPushException, StackIndexError


class Stack(object):
    """
    This class is a basic implementation of a stack.
    This implementation supports push, pop, load and swap
    """
    MAX_STACK_VALUE = 0xff

    def __init__(self):
        self.__stack_list = []

    @property
    def stack(self):
        return self.__stack_list

    def _is_idx_in_bounds(self, idx):
        """
        Checks if a given index is out of the stack bounds

        :param idx: Index to check for bounds within the stack
        :return: If the index is out of bounds
        """
        return idx >= len(self.__stack_list)

    def push(self, value):
        """
        Pushes a value to the stack. The value must be under 0xff (256)

        :param value: The value to push to the stack
        """
        if value > Stack.MAX_STACK_VALUE:
            raise StackPushException(
                "Cannot push a value to the stack which is greater than {}".format(Stack.MAX_STACK_VALUE))

        self.__stack_list.insert(0, value)

    def load(self, offset):
        """
        Pushes the value at stack[offset] to the stack.

        :param offset: The offset from the beginning of the stack in bytes
        """

        if self._is_idx_in_bounds(offset):
            raise StackOutOfBounds("Stack value offset is out of bounds.")

        self.push(self.__stack_list[offset])

    def swap(self, index):
        """
        Swaps the element at HEAD (0) with the element at index.

        :param index: The index of the element to swap the head of the stack with
        """
        if self._is_idx_in_bounds(index):
            raise StackOutOfBounds("Swap index is out of stack bounds")

        if index == 0:
            self.pop()

        self.__stack_list[0], self.__stack_list[index] = self.__stack_list[index], self.__stack_list[0]

    def pop(self):
        """
        Pops an element from the stack

        :return: The value of the popped element
        """
        if len(self.__stack_list) == 0:
            raise StackIndexError("Cannot pop element from an empty stack")

        return self.__stack_list.pop(0)

    def empty(self):
        return not len(self.__stack_list)
