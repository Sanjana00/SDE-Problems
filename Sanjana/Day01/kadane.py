def kadane(arr: [int]) -> int:
    m = arr[0]
    s = 0
    for ele in arr:
        s += ele
        m = max(m, s)
        s = max(s, 0)
    return m

arr = [int(x) for x in input().split()]
print(kadane(arr))

'''

Finding maximum sum of subarray

'''
