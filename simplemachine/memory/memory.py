from .exceptions import MemoryPermissionsError
import stack


class Memory(object):
    """
    This class manages the memory of the simplemachine.
    It is used to manage the code and stack.
    """

    def __init__(self):
        self.__stack = stack.Stack()  # RW
        self.__code = []  # RO
        self.__code_is_set = False

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, code):
        """
        Sets the code to a given value
        The code can only be set once

        :param code: The code to set
        """
        if self.__code_is_set:
            raise MemoryPermissionsError("The code section can only be initialized and not written")

        self.__code_is_set = True
        self.__code = code

    @property
    def stack(self):
        return self.__stack
