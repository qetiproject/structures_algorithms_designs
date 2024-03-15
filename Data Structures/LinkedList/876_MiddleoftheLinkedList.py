# https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
    
# Time: O(N)
# Space: O(1)
def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        temp = head
        while temp:
             length += 1
             temp = temp.next
        
        middle = length // 2
        for i in range(middle):
             head = head.next
        return head