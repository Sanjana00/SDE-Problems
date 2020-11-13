def is_palin(s: str) -> bool:
    return s == s[::-1]

def palin_partition(s: str, i: int, j: int) -> int:
    if i >= j or is_palin(s[i : j + 1]):
        return 0
    ans = float('inf')
    for k in range(i, j):
        count = 1 + palin_partition(s, i, k) + palin_partition(s, k + 1, j)
        ans = min(ans, count)
    return ans

s = input()
print(palin_partition(s, 0, len(s) - 1))
