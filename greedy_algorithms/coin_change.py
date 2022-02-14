

"""
Algorithm
1. Create a list of available denominations in the decreasing order.
    d = [100, 50, 25]
2. Create variable number_of_coins = 0
3. for c in d:
    a. number_of_coins += cents // c
    b. cents = cents % c
4. return number_of_coins
"""
def coin_making(cents):
    COINS = [100, 50, 25, 10, 5, 1]
    num_of_coins = 0
    for coin in COINS:
        num_of_coins += cents // coin
        cents %= coin
    return num_of_coins


if __name__ == '__main__':
    print(coin_making(125))