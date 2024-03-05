# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Time: O(N)
# Space: O(1)
def swapNodes(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    left, right = head, head 

    curr_index = 1
    curr_pointer = head

    while curr_pointer:
        if curr_index == k:
            left = curr_pointer
        elif curr_index > k:
            right = right.next
        curr_index += 1
        curr_pointer = curr_pointer.next

    left.val, right.val = right.val, left.val
    return head