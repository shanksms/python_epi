

def gcd(x, y):
    if y > x:
        y, x = x, y
    return x if y == 0 else gcd(y, x % y)

if __name__ == '__main__':
    print(gcd(3, 9))