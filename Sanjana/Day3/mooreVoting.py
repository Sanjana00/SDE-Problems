def mooreVoting(arr: [int]) -> int:
    c = 0
    ele = 0
    for element in arr:
        if c == 0:
            ele = element
        if ele == element:
            c += 1
        else:
            c -= 1
    return ele

arr = [int(x) for x in input().split()]
print("The majority element is: {}".format(mooreVoting(arr)))

'''
Find the majority element in the array (present > n // 2 times).

Time complexity = O(n)

Intuition: Neutralisation (similar to acid-base reactions?)
'''
