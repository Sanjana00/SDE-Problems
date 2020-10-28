def job_sequencing(arr: [(str, int, int)]) -> [str]:
    intervals = {}
    for name, deadline, profit in arr:
        copy = deadline
        while copy in intervals and copy > 0:
            copy -= 1
        if copy > 0:
            intervals[copy] = name
    return intervals.values()

t = int(input())
arr = []
for _ in range(t):
    item = input().split()
    item[1], item[2] = int(item[1]), int(item[2])
    arr.append(item)

arr.sort(key = lambda x: x[2], reverse = True)

print(*job_sequencing(arr))
