def fractional_knapsack(arr: [int], k: int) -> int:
    total_value = 0
    total_weight = 0
    for value, weight in arr:
        if total_weight + weight <= k:
            total_value += value
            total_weight += weight
        else:
            total_value += (k - total_weight) * value / weight
            break
    return int(total_value)
    
k = int(input())
values = [int(x) for x in input().split()]
weights = [int(x) for x in input().split()]

arr = list(zip(values, weights))
arr.sort(key = lambda x: x[0] / x[1], reverse = True)
print(fractional_knapsack(arr, k))
