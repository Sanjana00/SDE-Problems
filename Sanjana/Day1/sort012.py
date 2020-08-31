#!/usr/bin/env python3
import sys

def dutchNationalFlag(n: int, arr: [int]) -> [int]:
    low, mid, high = 0, 0, n - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 2:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
        else:
            mid += 1
    return arr

n = int(sys.argv[1])
arr = [int(x) for x in sys.argv[2:]]
print(*dutchNationalFlag(n, arr))

'''
Sort an array consisting of 0s, 1s and 2s without using extra space or any sorting algo.

Three pointers - low, mid and high
low points to position before which all elements are 0
high points to position after which all elements are 2

Time complexity O(N)
Space complexity O(1)

'''
