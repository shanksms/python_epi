def countPairsWithDifference2(numbers, k):
    li = []
    for i in range(len(numbers)):
        sub_li = numbers[:i] + numbers[i + 1:]
        if numbers[i] + k in sub_li:
            li.append((numbers[i], numbers[i] + k))
    li = [(numbers[i], numbers[i] + k) for i in range(len(numbers)) if numbers[i] + k in numbers[:i] + numbers[i + 1:]]
    # # li = [(a,a+k) for a in numbers if a+k in numbers]
    return len(list(set(li)))

if __name__ == '__main__':
    print(countPairsWithDifference2([1, 1, 2, 2, 3, 3], 1))