#!/usr/bin/env python3
import sys

def repeatMissing(n: int, arr: [int]) -> (int, int):
    S = n * (n + 1) // 2
    S2 = n * (n + 1) * (2 * n + 1) // 6
    s, s2 = 0, 0
    for ele in arr:
        s += ele
        s2 += (ele * ele)
    minus = S - s
    plus = (S2 - s2) // minus
    return (plus + minus) // 2, (plus - minus) // 2

n = int(sys.argv[1])
arr = [int(x) for x in sys.argv[2:]]
print("The missing number is {} and the duplicate number is {}".format(*repeatMissing(n, arr)))

'''

Array of size n containing numbers from 1 to n. One number is missing and one number is present twice.
Find missing and duplicate numbers.

S(n) = 1 + 2 + 3 + ... + n = n * (n + 1) // 2
S2(n) = 1 ** 2 + 2 ** 2 + 3 ** 2 + ... + n ** 2 = n * (n + 1) * (2 * n + 1) // 6

Let s = sum of array elements
and s2 = sum of sqaured array elements

S(n) - s = missing number - duplicate number
S2(n) - s2 = (missing number ** 2) - (duplicate number ** 2)
           = (missing number + duplicate number) * (missing number - duplicate number)

missing number + duplicate number = (S2(n) - s2) // (S(n) - s) = X (let)
missing number - duplicate number = S(n) - s = Y (let)

Therefore,
missing number = (X + Y) // 2
duplicate number = (X - Y) // 2

Time complexity O(N)
Space complexity O(1)

'''
