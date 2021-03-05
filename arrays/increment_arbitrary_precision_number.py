def add_one(A):
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] == 10:
            A[i] = 0
            A[i - 1] += 1
        else:
            break
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A
if __name__ == '__main__':
    print(add_one([9, 9]))