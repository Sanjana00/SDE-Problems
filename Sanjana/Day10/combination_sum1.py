def combinations(arr, target, collection, result):
    if target < 0:
        return
    if target == 0:
        result.add(tuple(sorted(collection)))
        return
    
    for element in arr:
        combinations(arr, target - element, collection + [element], result)

def combinationSum(arr, target):
    result = set()
    combinations(arr, target, [], result)
    
    return result

arr = [int(x) for x in input().split()]
target = int(input())

for combination in combinationSum(arr, target):
    print(*combination)
