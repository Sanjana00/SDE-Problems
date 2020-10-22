n = int(input())
arr = [int(x) for x in input().split()]
indices = {}
for i, ele in enumerate(arr):
    if n - ele in indices:
        print('{} {}'.format(i, indices[n - ele]))
        break
    indices[ele] = i
    
'''
Find the pair of indices whose elements add up to given number

Must not repeat any element - pair can be in any order

Time complexity = O(n)

Approach: Store element along with its index in hash table until both numbers have been encountered
'''
