from queue import PriorityQueue


def kLargest(arr, k):
    pq = PriorityQueue()
    # code here
    for element in arr:
        pq.put(-element)
    result = []
    for i in range(k):
        result.append(-pq.get())
    return result
