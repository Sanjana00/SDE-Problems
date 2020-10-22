def maxStockProfit(arr: [int]) -> int:
    low = arr[0]
    profit = 0
    for ele in arr:
        if ele < low:
            low = ele
        else:
            profit = max(profit, ele - low)
    return profit

arr = [int(x) for x in input().split()]
print(maxStockProfit(arr))

'''

Given an array of stock prices where arr[i] = price on i th day, find maximum profit if you are to buy and sell one stock.
You can only sell a stock if you have bought it first.

Time Complexity = O(N)

'''
