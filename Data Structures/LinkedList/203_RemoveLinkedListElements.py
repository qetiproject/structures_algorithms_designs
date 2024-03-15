# https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Time: O(N)
# Space: O(1)
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp = head
        while temp and temp.next:
            if temp.next.val == val:
                temp.next  = temp.next.next
            else:
                temp = temp.next
        if head and head.val == val:
            head = head.next
        return head
    
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_head = ListNode(-1)
        dummy_head.next = head

        current_node = dummy_head
        while dummy_head.next != None:
            if current_node.next.val == val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
        return dummy_head.next