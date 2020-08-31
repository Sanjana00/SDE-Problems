#!/usr/bin/env python3
import sys

def hareTortoise(arr: [int]) -> int:
    slow = arr[arr[0]]
    fast = arr[arr[arr[0]]]
    while slow != fast:
        slow = arr[slow]
        fast = arr[arr[fast]]
    fast = arr[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[slow]
    return slow

arr = [int(x) for x in sys.argv[1:]]
print("Duplicate: {}".format(hareTortoise(arr)))

'''

The array contains numbers from 1 to n where only one number is present more than once

The duplicate number creates a cycle

Time complexity O(N)
Space complexity O(1)

'''
