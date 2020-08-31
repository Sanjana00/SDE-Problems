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

n = int(input())
arr = [int(x) for x in input().split()]
print("The missing number is {} and the duplicate number is {}".format(*repeatMissing(n, arr)))
