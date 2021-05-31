import heapq


def heapify_example(_list : []):
    """
    heapify rearranges list elements in the form of min heap.
    2K + 1, 2K + 2 where k starts with 0
    :param _list:
    :return:
    """
    heapq.heapify(_list)
    return _list


def heap_sort_example(_iterable):
    h = []
    for element in _iterable:
        heapq.heappush(h, element)
    return [heapq.heappop(h) for _ in range(len(_iterable))]


if __name__ == '__main__':
    print(heapify_example([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))
    print(heap_sort_example([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))

