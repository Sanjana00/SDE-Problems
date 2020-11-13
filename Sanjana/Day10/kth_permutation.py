from functools import reduce
from math import factorial

n = int(input())
k = int(input()) - 1

result = [0] * n

nums = list(range(1, n + 1))

for i in range(n):
    result[i] = nums[k // factorial(n - 1 - i)]
    k = k % factorial(n - i - 1)
    nums.remove(result[i])
    
print(reduce(lambda x, y: x * 10 + y, result))
