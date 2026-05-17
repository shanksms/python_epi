

def SieveOfEratosthenes(num : int):
    bool_list = [True] * (num + 1)
    i = 2
    while i*i <= num:
        if bool_list[i]:
            for j in range(i*i, num+1, i):
                bool_list[j] = False
        i += 1
    result = []
    for idx in range(2, num +1):
        if bool_list[idx]:
            result.append(idx)
    return result



if __name__ == '__main__':
    n = 100
    primes_n = set(SieveOfEratosthenes(n))
    print(primes_n)
    m = 30
    primes_m = [x for x in primes_n if x < m]
    for i in range(len(primes_m)):
        _sum = primes_m[i]
        for j in range(i+1, len(primes_m)):
            _sum += primes_m[j]
            if _sum in primes_n:
                print(_sum)

