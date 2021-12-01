import functools
import string


def decode(column):
    """
    column could be 'A', 'B', 'AA' etc
    :param column:
    :return: A --> 1, B --> 2, Z --> 26 etc
    """
    return functools.reduce(lambda result, c: 26 * result + ord(c) - ord('A') + 1, column, 0)


def encode(column_number):
    """
    1 -> A, 2 -> B, 26 > Z, 27 -> AA
    :param column_number:
    :return:
    """
    # generate a dictionary of letters and numbers
    num_letter_dict = {c: chr(64 + c) for c in range(1, 27)}
    ls = []

    while column_number > 0:
        rem = column_number % 26
        if rem == 0:
            ls.append('Z')
            column_number = column_number // 26 - 1
        else:
            ls.append(
                chr(rem - 1 + ord('A'))
            )
            column_number = column_number // 26
    print(ls)

if __name__ == '__main__':
    encode(27)