def max_coins(coins: [int], size: int) -> int:
    n = size // 3
    coins.sort()
    my_coins = 0
    for i in range(n, size, 2):
        my_coins += coins[i]
    return my_coins

coins = [int(x) for x in input().split()]

print(max_coins(coins, len(coins)))
