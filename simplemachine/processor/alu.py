"""
This module contains the implementation of the low level arithmetic operations.
"""

from ctypes import c_byte as byte
from ctypes import c_ubyte as ubyte


def one_byte_result(operation):
    """
    Used to make sure an arithmetic operation result is one byte only

    :param operation: The function which executes the operation
    :return:
    """
    def f(*args):
        return byte(operation(*args)).value

    return f


class ArithmeticLogicUnit(object):
    """
    This class contains the arithmetic operations implementation
    """
    @staticmethod
    @one_byte_result
    def add(first_operand, second_operand):
        return first_operand + second_operand

    @staticmethod
    @one_byte_result
    def subtract(first_operand, second_operand):
        return first_operand - second_operand

    @staticmethod
    @one_byte_result
    def multiply(first_operand, second_operand):
        return first_operand * second_operand

    @staticmethod
    def divide(first_operand, second_operand):
        """
        Divides the first operand by the second

        :param first_operand: The dividend
        :param second_operand: The divisor
        :return: A tuple -> (division result, remainder)
        """
        first_operand, second_operand = ubyte(first_operand).value, ubyte(second_operand).value
        return ubyte(first_operand / second_operand).value, ubyte(first_operand % second_operand).value
