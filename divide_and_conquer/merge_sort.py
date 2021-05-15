def merge(left, arr, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    A = [arr[left + x] for x in range(0, n1)]
    B = [arr[mid + 1 + x] for x in range(0, n2)]

    i, j, k = 0, 0, left
    while i < n1 and j < n2:
        if A[i] < B[j]:
            arr[k] = A[i]
            k += 1
            i += 1
        else:
            arr[k] = B[j]
            k += 1
            j += 1
    while i < n1:
        arr[k] = A[i]
        k += 1
        i += 1
    while j < n2:
        arr[k] = B[j]
        k += 1
        j += 1




def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(left, arr, mid, right)


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    n = len(arr)
    print("Given array is")
    for i in range(n):
        print("%d" % arr[i], end=' '),

    merge_sort(arr, 0, n - 1)
    print("\n\nSorted array is")
    for i in range(n):
        print("%d" % arr[i], end=' '),