from simplemachine.utils.exceptions import EmulatorException


class NoExecutorFound(EmulatorException):
    """
    Raised when no executor function was found for a given opcode
    """
    pass


class IPOutOfBounds(EmulatorException):
    """
    Raised when the IP value is not in a valid code range
    """
    pass
