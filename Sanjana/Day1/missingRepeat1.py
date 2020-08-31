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
