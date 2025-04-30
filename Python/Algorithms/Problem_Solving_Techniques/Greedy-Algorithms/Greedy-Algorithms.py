import time 

def TotalCoins(coin:int):
    resulte = 0
    coins = [200, 100, 50, 20, 10, 5, 1]
    for i in coins:
        while coin >= i :
            coin -= i
            resulte += 1
        if coin < 1 :
            return resulte
    return resulte


start = time.time()

my_coins = 193467271234

print(TotalCoins(my_coins))

final = time.time()

print(final - start)


def TotalCoins(coin:int):
    resulte = 0
    coins = [200, 100, 50, 20, 10, 5, 1]
    for i in coins:
        if coin % i == 0 :
            return (coin / i) + resulte
        else :
            resulte += (coin // i)
            coin -= (i * (coin//i))


start = time.time()

print(TotalCoins(my_coins))

final = time.time()

print(final - start)
