"""
This module is used to decode opcodes.
The decode process is basically finding a matching executor function.
An executor function should contain all of the login in order to run the given opcode.
"""
from simplemachine.processor.exceptions import NoExecutorFound


def register_opcode(opcode):
    """
    Registers an opcode and function pair to the decoder
    Later when the decoder decodes an opcodes it will look up in the registered functions.

    :param opcode: The opcode to register the function to
    """

    def f(executor):
        Decoder.CONSTANT_OPCODES[opcode] = executor
        return executor

    return f


def register_range_opcode(range_start, range_end):
    """
    Registers an opcode range and function to the decoder
    Later when the decoder decodes an opcodes it will look up in the registered functions.

    Matches an executor when an opcode value will be between the start and the end range

    :param range_start: The minimum value of the opcode (including the start)
    :param range_end: The maximum value of the opcode (including the end)
    """
    def f(executor):
        Decoder.RANGE_OPCODES[(range_start, range_end)] = executor
        return executor

    return f


class Decoder(object):
    CONSTANT_OPCODES = {}
    RANGE_OPCODES = {}

    @staticmethod
    def decode(opcode):
        """
        Decodes a given opcode based on the current opcode -> executor mappings

        An opcode may be a constant or range. A range opcode contains a parameter in the opcode value.

        :param opcode: The opcode value to decode
        :return: An executor and it's arguments
        """
        if opcode in Decoder.CONSTANT_OPCODES:
            # A constant opcode doesn't receive arguments
            return Decoder.CONSTANT_OPCODES[opcode], tuple()

        for (range_min, range_max), executor in Decoder.RANGE_OPCODES.items():
            if range_min <= opcode <= range_max:
                # The argument for a range opcode is the opcode value minus the min opcode value
                return executor, (opcode - range_min,)

        raise NoExecutorFound("Cannot decode opcode {}. No executor found!".format(opcode))
