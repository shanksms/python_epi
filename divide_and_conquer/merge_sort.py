def merge(arr, l, m, r):
    pass


def merge_sort(arr, l, r ):
    m = (l + r)//2
    merge_sort(arr, l, m)
    merge_sort(arr, m + 1, r)
    merge(arr, l, m, r)
    