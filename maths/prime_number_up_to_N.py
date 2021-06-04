

def SieveOfEratosthenes(num : int):
    bool_list = [True]*(num + 1)
    i = 2
    while i * i <= num:
        if bool_list[i]:
            #i is a prime number
            for j in range(i * i, num + 1, i):
                bool_list[j] = False
        i += 1

    for i in range(2, num + 1):
        if bool_list[i]:
            print(i, end=" ")


if __name__ == '__main__':
    n = 30
    SieveOfEratosthenes(n)
