from itertools import permutations

s = input()
perms = permutations(s)
for perm in perms:
    print(perm)
