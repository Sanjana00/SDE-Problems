def max_meetings(arr: [(int, int)]) -> int:
    count = 0
    end = 0
    for start, finish in arr:
        if start >= end:
            count += 1
            end = finish
    return count

starts = [int(x) for x in input().split()]
finishes = [int(x) for x in input().split()]

timestamps = list(zip(starts, finishes))
    
timestamps.sort(key = lambda x: x[1])

print(max_meetings(timestamps))
