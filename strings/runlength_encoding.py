
def encode(input_text):
    '''
    aab --> a2b
    :param input_text:
    :return: encoded text
    Algorithm:
    1. initialize count = 1
    2. for i = 1 to len(input_string) - 1
        a. prev = input_string[i - 1]
        b. current = input_string[i]
        c. if current == prev
                count += 1
            else
                 li.append(prev)
                 li.append(str(count))
                 count = 1
    3. li.append(input_text[i])
    4. li.append(str(count))
    '''
    if not input_text:
        return []
    count = 1
    li = []
    i = 0
    for i in range(1, len(input_text)):
        prev = input_text[i - 1]
        current = input_text[i]
        if current == prev:
            count += 1
        else:
            li.append(prev)
            li.append(str(count))
            count = 1
    li.append(input_text[i])
    li.append(str(count))
    return ''.join(li)


def decode(encoded_string):
    li = list()
    for i in range(1, len(encoded_string), 2):
        count = int(encoded_string[i])
        string_to_add = encoded_string[i - 1] * count
        li.append(string_to_add)
    return ''.join(li)




if __name__ == '__main__':
    print(encode('aab'))
    print(decode(''))