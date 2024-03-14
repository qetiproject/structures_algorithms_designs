# https://leetcode.com/problems/min-cost-climbing-stairs/

from typing import List

# Time: O(N)
# Space: O(N)
memo = {1:1, 2:2}
def minCostClimbingStairs(cost: List[int]) -> int:
    n = len(cost)
    result = [0] * (n + 1)

    result[0] = 0
    result[1] = cost[0]
    
    for i in range(2, n + 1):
        result[i] = cost[i - 1] + min(result[i - 1], result[i - 2])
        
    return min(result[n], result[n - 1])
    
# Time: O(N)
# Space: O(1)
def minCostClimbingStairs(cost: List[int]) -> int:
    for i in range(2, len(cost)):
        cost[i] += min(cost[i-2], cost[i-1])
    return min(cost[len(cost)-2], cost[len(cost)-1])
