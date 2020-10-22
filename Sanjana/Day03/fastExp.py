def fastExp(x: float, n: float) -> int:
    ans = 1
    neg = n < 0
    n = -n if n < 0 else n
    while n > 0:
        if n % 2 == 1:
            ans *= x
            n -= 1
        else:
            x *= x
            n /= 2
    if neg:
        return 1 / ans
    return ans

x = float(input())
n = float(input())
print(fastExp(x, n))

'''
Find x to the power of n

Time complexity = O(log n)
Space complexity = O(1)
'''
