from simplemachine.utils.exceptions import EmulatorException


class MemoryPermissionsError(EmulatorException):
    pass


class StackException(EmulatorException):
    pass


class StackPushException(EmulatorException):
    pass


class StackIndexError(EmulatorException):
    pass


class StackOutOfBounds(StackIndexError):
    pass
