
from functools import reduce
import string
def string_to_int_short_version(input_str):
    #https://realpython.com/python-reduce-function/
    #https://www.geeksforgeeks.org/python-string-digits/
    return reduce(lambda running_sum, character : 10*running_sum + string.digits.index(character)
                  , input_str[input_str[0] == '-':], 0) * (-1 if input_str[0] == '-' else 1)
def string_to_int(input_str):
    result = 0
    is_negative = input_str[0] == '-'
    '''
    in String slicing if is_negative is true, it will behave like 1. if 
    it is false, it behave like 0
    '''
    for c in input_str[is_negative:]:
        result = 10*result + string.digits.index(c)
    return result * (-1 if is_negative else 1)
if __name__ == '__main__':
    print(string_to_int_short_version('123'))
    print(string_to_int_short_version('-123'))
    print(string_to_int('-123'))




