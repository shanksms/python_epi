from math import fsum


def avg(nums):
    if not nums:
        raise ValueError('can not be None')
    return fsum(nums) / len(nums)


def covariance(nums1, nums2):
    """
    Algorithm:
    lst1 = []
    lst2 = []
    1. Calculate avg of both numbers
    2. for n in nums1:
          lst1.append(n - avg1)
    3. for n in nums2:
          lst2.append(n - avg2)
    4. multiply lst1 with lst2. Sum the result
          lst3 = sum([n1 * n2 for n1, n2 in zip(lst1, lst2)])
    5. lst3/ len(nums1)

    :param nums1:
    :param nums2:
    :return:
    """
    avg1 = avg(nums1)
    avg2 = avg(nums2)
    distance_from_avg1 = [num - avg1 for num in nums1]
    distance_from_avg2 = [num - avg2 for num in nums2]
    sum_of_multiplications = sum([num1 * num2 for num1, num2 in zip(distance_from_avg1, distance_from_avg2)])
    return sum_of_multiplications / (len(nums1) - 1)


if __name__ == '__main__':
    temperatures = [14.2, 16.4, 15.2, 22.6, 17.2]
    ice_cream_sales = [215, 325, 332, 445, 408]
    print(covariance(temperatures, ice_cream_sales))


