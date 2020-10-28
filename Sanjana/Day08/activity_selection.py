def activity_selection(arr: [(int, int)]) -> [int]:
    end = 0
    activities = []
    for i, (start, finish) in enumerate(arr):
        if start >= end:
            activities.append(i + 1)
            end = finish
    return activities

starts = [int(x) for x in input().split()]
finishes = [int(x) for x in input().split()]

timestamps = list(zip(starts, finishes))
    
timestamps.sort(key = lambda x: x[1])

print(*activity_selection(timestamps))
