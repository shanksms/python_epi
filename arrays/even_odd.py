def even_odd(A):
    even_counter, odd_counter = 0, len(A) - 1
    while even_counter < odd_counter:
        if A[even_counter] % 2 == 0:
            even_counter += 1
        else:
            A[even_counter], A[odd_counter] = A[odd_counter], A[even_counter]
            odd_counter -= 1
    return A
if __name__ == '__main__':
    print(even_odd([1, 2, 3, 4, 5, 6]))