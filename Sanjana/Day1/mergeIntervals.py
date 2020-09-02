def is_merge(int1: (int, int), int2: (int, int)) -> bool:
    return int2[0] <= int1[1]

def merged(int1: (int, int), int2: (int, int)) -> (int, int):
    return (min(int1[0], int2[0]), max(int1[1], int2[1]))

def mergeIntervals(intervals: [(int, int)]) -> [(int, int)]:
    intervals.sort()
    result = [intervals[0]]
    for interval in intervals:
        if is_merge(result[-1], interval):
            result[-1] = merged(result[-1], interval)
        else:
            result.append(interval)
    return result

n = int(input())
intervals = [0] * n
for i in range(n):
    intervals[i] = tuple(int(x) for x in input().split())
print(mergeIntervals(intervals))
