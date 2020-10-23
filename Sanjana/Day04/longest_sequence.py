arr = set([int(x) for x in input().split()])
max_count = 1
for ele in arr:
    if ele - 1 in arr:
        continue
    count = 1
    while ele + 1 in arr:
        ele += 1
        count += 1
    max_count = max(max_count, count)
print(max_count)

'''
Count the length of the longest sequence of consecutive integers present in the array

Time complexity = O(N)

'''
