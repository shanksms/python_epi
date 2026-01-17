

def gcd(x, y):
    if x > y:
        x, y = y, x
    if x == 0:
        return y
    elif y == 0:
        return x
    else:
        return gcd(y % x, x)

if __name__ == '__main__':
    print(gcd(8, 7))