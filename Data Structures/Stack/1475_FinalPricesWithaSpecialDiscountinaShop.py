# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []

        i = 0
        while i < len(prices):
            j = i + 1
            while j < len(prices) and prices[j] < prices[i]:
                j += 1
            if j < len(prices):
                stack.append(prices[i] - prices[j])
            else:
                stack.append(prices[i])
            i += 1
        return stack