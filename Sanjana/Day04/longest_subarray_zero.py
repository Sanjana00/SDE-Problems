arr = [int(x) for x in input().split()]
_sum = 0
count = 0
ans = []
sums = {0 : -1}
for i, ele in enumerate(arr):
    _sum += ele
    if _sum not in sums:
        sums[_sum] = i
        continue
    if i - sums[_sum] > count:
        count = i - sums[_sum]
        ans = arr[sums[_sum] + 1: i + 1]
print(count)
print(*ans)

'''
Find the length of the longest subarray that has a sum = 0

Time Complexity = O(N)

Approach: Traverse the array and keep updating the sum. Keep a hash table of the value of sum and where that value was first encountered.
If a sum value is repeated, count is updated to current index minus the index at which sum first appeared in array. The maximum count is kept.

Visualization:

S + 0 = S
Therefore, if S occurs at x and repeats at y, then the elements between x and y (arr[x + 1: y + 1]) must add up to 0.

'''
