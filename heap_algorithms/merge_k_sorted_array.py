import heapq


def merge_sorted_arrays(sorted_arrays):
    _heap = []
    sorted_array_iters = [iter(x) for x in sorted_arrays]
    for i, sorted_array_iter in enumerate(sorted_array_iters):
        next_element = next(sorted_array_iter, None)
        if next_element is not None:
            heapq.heappush(_heap, (next_element, i))
    result = []
    while _heap:
        smallest_entry, smallest_entry_iter_index = heapq.heappop(_heap)
        result.append(smallest_entry)
        smallest_entry_iter = sorted_array_iters[smallest_entry_iter_index]
        next_element = next(smallest_entry_iter, None)
        if next_element is not None:
            heapq.heappush(_heap, (next_element, smallest_entry_iter_index))
    return result

if __name__ == '__main__':
    print(merge_sorted_arrays([[1, 8], [3, 7], [10, 11]]))

