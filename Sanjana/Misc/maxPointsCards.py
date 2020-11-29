
def maxScore(cardPoints: List[int], k: int) -> int:
    if k == 0:
        return 0
    if len(cardPoints) <= k:
        return sum(cardPoints)

    left = 0
    right = k
    maxSum = sum(cardPoints[left:right])
    currSum = maxSum
    while k > 0:
        k -= 1
        left -= 1
        right -= 1
        currSum += cardPoints[left]
        currSum -= cardPoints[right]
        maxSum = max(maxSum, currSum)
    return maxSum
    
    
'''
    
Sliding window of length k which folds around the list such that it encloses k elements from both ends of the list. Find instance where sum is maximum.

'''
