# https://leetcode.com/problems/merge-nodes-in-between-zeros/

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# Time: O(N)
# Space: O(1)
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr = head
        curr = curr.next
        sum = 0

        while curr:
            if curr.val == 0:
                dummy = dummy.next
                dummy.val = sum
                sum = 0
            else:
                sum += curr.val
            curr = curr.next
        dummy.next = None
        return head.next