def maxProfit(prices) -> int:
    if len(prices) <= 1:
        return 0
    currMin = min(prices[0], prices[1])
    currMaxProfit = 0
    if prices[0] == currMin:
        currMaxProfit = prices[1] - prices[0]
        
    for i in range(2, len(prices), 1):
        if prices[i] - currMin > currMaxProfit:
            currMaxProfit = prices[i] - currMin
        elif prices[i] - currMin < 0:
            currMin = prices[i]
    return currMaxProfit
    
print(maxProfit([7,1,5,3,6,4]))