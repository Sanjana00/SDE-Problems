from heapq import heapify, heappushpop

def kthLargest(arr: [int], k: int) -> int:
    minHeap = arr[:k]
    heapify(minHeap)
    for element in arr[k:]:
        heappushpop(minHeap, element)
    return minHeap[0]
