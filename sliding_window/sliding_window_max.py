

def naive_approach(arr, k):
    result = []
    for i in range(len(arr)-(k-1)):
        sub_arr = arr[i:i+k]
        result.append(max(sub_arr))
    return result


if __name__ == '__main__':
    assert  [3, 3, 5, 5, 6, 7] == naive_approach([1, 3, -1, -3, 5, 3, 6, 7], 3)