def is_palindrome(input_str):
    #this produces a generator object: (input_str[i] == input_str[~i] for i in range(len(input_str)//2))
    # all function iterates over it by calling next
    return all((input_str[i] == input_str[~i] for i in range(len(input_str)//2)))

if __name__ == '__main__':
    print(is_palindrome('aba'))
    print(is_palindrome('abc'))