# https://leetcode.com/problems/first-unique-character-in-a-string/


from collections import defaultdict
from typing import Deque

# Time: O(N)
# Space: O(N)
# class Solution:
#     def firstUniqChar(self, string: str) -> int:
#         char_counts = {}
#         for i, char in enumerate(string): # O(N)
#             char_counts[char] = char_counts.get(char, 0) + 1
        
#         for i, char in enumerate(string): # O(N)
#             if char_counts[char] == 1:
#                 return i

#         return -1
    
# Time: O(N)
# Space: O(N)
class Solution:
    def firstUniqChar(self, string: str) -> int:
        char_counts = defaultdict(int)
        queue = Deque()
        for i, char in enumerate(string): # O(N)
            char_counts[char] += 1
            queue.append((char, i))
            while queue and char_counts[queue[0][0]] > 1:
                queue.popleft()

        return queue[0][1] if queue else -1 