
def method_1(arr):

    count = 0
    size = len(arr)
    for i in range(0, size):
        for j in range(i + 1, size):
            if arr[i] > arr[j]:
                count += 1
    return count


# Python 3 program to count inversions in an array

# Function to Use Inversion Count
def mergeSort(arr, n):
    # A temp_arr is created to store
    # sorted array in merge function
    temp_arr = [0] * n
    return _mergeSort(arr, 0, n - 1)


# This Function will use MergeSort to count inversions

def _mergeSort(arr, left, right):
    # A variable inv_count is used to store
    # inversion counts in each recursive call

    inv_count = 0

    # We will make a recursive call if and only if
    # we have more than one elements

    if left < right:
        # mid is calculated to divide the array into two subarrays
        # Floor division is must in case of python

        mid = (left + right) // 2

        # It will calculate inversion
        # counts in the left subarray

        inv_count += _mergeSort(arr,
                                left, mid)

        # It will calculate inversion
        # counts in right subarray

        inv_count += _mergeSort(arr,
                                mid + 1, right)

        # It will merge two subarrays in
        # a sorted subarray

        inv_count += merge(arr, left, mid, right)
    return inv_count


# This function will merge two subarrays
# in a single sorted subarray
def merge(arr, left, mid, right):

    inv_count = 0
    n1 = mid + 1 - left
    n2 = right - mid
    L = [arr[x + left] for x in range(0, n1)]
    R = [arr[x + 1 + mid] for x in range(0, n2)]
    i = 0  # Starting index of left subarray
    j = 0  # Starting index of right subarray
    k = left  # Starting index of to be sorted subarray

    # Conditions are checked to make sure that
    # i and j don't exceed their
    # subarray limits.

    while i < n1 and j < n2:

        # There will be no inversion if arr[i] <= arr[j]

        if L[i] <= R[j]:
            arr[k] = L[i]
            k += 1
            i += 1
        else:
            # Inversion will occur.
            arr[k] = R[j]
            inv_count += (mid - left -i + 1)
            k += 1
            j += 1

    # Copy the remaining elements of left
    # subarray into temporary array
    while i < n1:
        arr[k] = L[i]
        k += 1
        i += 1

    # Copy the remaining elements of right
    # subarray into temporary array
    while j < n2:
        arr[k] = R[j]
        k += 1
        j += 1


    return inv_count





if __name__ == '__main__':
    # Driver Code
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    rev_arr = sorted(arr, reverse=True)
    n = len(arr)
    print("Number of inversions are",
          method_1(rev_arr))
    print("Number of inversions are",
          mergeSort(rev_arr, n))