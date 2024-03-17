# https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Time: O(N)
# Space: O(N)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        been = set()
        while head:
            if head in been:
                return True
            been.add(head)
            head = head.next
        return False
    
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_pointer, fast_pointer = head, head
        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if slow_pointer == fast_pointer:
                return True
        return False