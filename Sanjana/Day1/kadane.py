def kadane(arr: [int]) -> int:
    m = arr[0]
    s = 0
    n = len(arr)
    for i in range(n):
        s += arr[i]
        m = max(m, s)
        s = max(s, 0)
    return m
