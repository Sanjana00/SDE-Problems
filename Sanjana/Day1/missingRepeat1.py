#!/usr/bin/env python3
import sys

def repeatMissing(n: int, arr: [int]) -> (int, int):
    freq = {}
    s = 0
    S = (n * (n + 1)) // 2
    for ele in arr:
        s += ele
        if ele in freq:
            dup = ele
        else:
            freq[ele] = 1
    miss = S - s + dup
    return miss, dup

n = int(sys.argv[1])
arr = [int(x) for x in sys.argv[2:]]
print("The missing number is {} and the duplicate number is {}".format(*repeatMissing(n, arr)))

'''

Array of size n contains numbers from 1 to n. One number is missing and another is present twice.
Find the missing and the duplicate numbers.

Dictionary used to check if number has been encountered more than once. If yes, then duplicate number has been located.

S(n) = 1 + 2 + 3 + ... + n = n * (n + 1) // 2

Therefore, missing number = S(n) - (sum of array - duplicate number)

Time complexity O(N)
Space complexity O(N)

'''
