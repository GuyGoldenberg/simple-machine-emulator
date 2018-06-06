from simplemachine.processor import decoder


def print_code(code):
    """
    Prints the code in a human readable way
    Converts decimal opcodes to function names with their parameters

    :param code: A list of decimal opcodes
    """
    for idx, b in enumerate(code):
        func, args = decoder.Decoder.decode(b)
        print "{}: {}{}".format(idx, func.__name__, "" if not len(args) else "({})".format(args[0]))
