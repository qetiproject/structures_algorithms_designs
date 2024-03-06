# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List

# Time: O(N)
# Space: O(1)
def maxProfit(prices: List[int]) -> int:
    if not prices:
        return 0
    
    min_purchase = prices[0]
    max_profit = 0

    for i in range(1, len(prices)):
        min_purchase = min(min_purchase, prices[i])
        max_profit = max(max_profit, prices[i] - min_purchase)

    return max_profit

print(maxProfit([7,1,5,3,6,4]))