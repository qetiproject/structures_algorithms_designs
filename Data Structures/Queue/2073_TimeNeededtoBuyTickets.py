# https://leetcode.com/problems/time-needed-to-buy-tickets/

from typing import Deque, List

# Time: O(N)
# Space: O(1)
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        result  = 0
        for i, ticket in enumerate(tickets):
            if i <= k:
                result += min(ticket, tickets[k])
            else:
                result += min(ticket, tickets[k] - 1)

        return result
    
# Time: O(N)
# Space: O(N)
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue  = Deque()
        for i, ticket in enumerate(tickets):
            queue.append(ticket, i)
        
        result = 0
        while queue:
            ticket, i = queue.popleft()
            result += 1
            ticket -= 1
            if ticket > 0:
                queue.append((ticket, i))
            if ticket == 0 and i == k:
                return result

        return result