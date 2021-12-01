import functools
import string


def decode(column):
    """
    column could be 'A', 'B', 'AA' etc
    :param column:
    :return: A --> 1, B --> 2, Z --> 26 etc
    """
    return functools.reduce(lambda result, c: 26 * result + ord(c) - ord('A') + 1, column, 0)

