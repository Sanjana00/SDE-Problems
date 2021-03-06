def mooreVoting(arr: [int]) -> int:
    c = 0
    n = 0
    for ele in arr:
        if c == 0:
            n = ele
        if ele == n:
            c += 1
        else:
            c -= 1
    return n

arr = [int(x) for x in input().split()]
print("The majority element is: {}".format(mooreVoting(arr)))

'''
Find the majority element in the array (present > n // 2 times).

Time complexity = O(n)

Intuition: Neutralisation (similar to acid-base reactions?)
'''
