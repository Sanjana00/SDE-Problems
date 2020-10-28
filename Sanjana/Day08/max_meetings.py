def max_meetings(arr: [(int, int)]) -> int:
    count = 0
    end = 0
    for finish, start in arr:
        if start >= end:
            count += 1
            end = finish
    return count

starts = [int(x) for x in input().split()]
finishes = [int(x) for x in input().split()]
size = len(starts)

timestamps = []

for i in range(size):
    timestamps.append((finishes[i], starts[i]))
    
timestamps.sort()

print(max_meetings(timestamps))
