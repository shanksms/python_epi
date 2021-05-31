def grade_school_multiplication(num1: [], num2: []):
    if len(num1) == 0 or len(num2)  == 0:
        raise ValueError('')
    sign = -1 if num1[0] < 0 ^ num2[0] < 0 else 1
    len1, len2 = len(num1), len(num2)
    result = [0] * (len1 + len2)
    for i in reversed(range(0, len1)):
        for j in reversed(range(0, len2)):
            result[i + j + 1] += num1[i] * num2[j]
            result[i + j] += result[i + j + 1] // 10
            result[i + j + 1] %= 10

    #remove leading zeros
    finalResult = result
    for i in range(len(result)):
        if result[i] != 0:
            finalResult = result[i:]
            break
    return finalResult * sign


if __name__ == '__main__':
    result = grade_school_multiplication([1, 2], [1, 2])
    print(result)
