# https://leetcode.com/problems/remove-nodes-from-linked-list/

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        head.next = self.removeNodes(head.next)
        if head.next and head.val < head.next.val:
            return head.next
        
        return head

# Time: O(N) # გასააზრებელი
# Space: O(1)
def reverseList(self, head : ListNode) -> ListNode:
    current = head
    prev = None
    while (current):
        old_next = current.next
        current.next = prev
        prev = current
        current = old_next
    return prev

def removeNodes(self, head: ListNode) -> ListNode:
    head = self.reverseList(head)
    maximum = -math.inf
    current = head
    prev = None

    while (current):
        tmp_next = current.next
        if current.val >= maximum:
            maximum = current.val
            if (prev):
                prev.next = current
                current.next = None
            else:
                head.next = None
            prev = current
        current = tmp_next
    return self.reverseList(head)

