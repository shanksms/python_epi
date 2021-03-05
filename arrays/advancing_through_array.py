
def minimum_steps_needed(A):
    max_reached_so_far = 0
    i = 0
    while i <= max_reached_so_far and max_reached_so_far < (len(A) - 1):
        max_reached_so_far = max(max_reached_so_far, i + A[i])
        i += 1

    return max_reached_so_far >= len(A) - 1

if __name__ == '__main__':
    print(minimum_steps_needed([3, 3, 1, 0, 2, 0, 1]))
    print(minimum_steps_needed([3, 2, 0, 0, 2, 0, 1]))

