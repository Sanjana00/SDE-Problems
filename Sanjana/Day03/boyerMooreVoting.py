def boyerMooreVoting(arr: [int]) -> [int]:
    l = len(arr)
    n1, n2, c1, c2 = -1, -1, 0, 0
    for ele in arr:
        if ele == n1:
            c1 += 1
        elif ele == n2:
            c2 += 1
        elif c1 == 0:
            n1 = ele
            c1 = 1
        elif c2 == 0:
            n2 = ele
            c2 = 1
        else:
            c1 -= 1
            c2 -= 1
    c1, c2 = 0, 0
    for n in arr:
        if n == n1:
            c1 += 1
        elif n == n2:
            c2 += 1
    ans = [n1, n2]
    if c1 <= l // 3:
        ans.remove(n1)
    if c2 <= l // 3:
        ans.remove(n2)
    return ans

arr = [int(x) for x in input().split()]
print(*boyerMooreVoting(arr))

'''
Find the element(s) which are present > n // 3 times in the array

Time complexity = O(n)

Intuition: Same as Moore Voting algo, neutralisation (but a little more complex this time)
'''
