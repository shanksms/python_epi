import functools
import string


def to_int(s):
    is_negative = True if s[0] == '-' else False
    if is_negative:
        s = s[1:]
    return_val = functools.reduce(lambda result, c: 10 * result + string.digits.index(c), s, 0)
    return -return_val if is_negative else return_val


if __name__ == '__main__':
    to_int('')
