# https://leetcode.com/problems/n-ary-tree-postorder-traversal/

from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.val)

            for child in node.children:
                stack.append(child)

        return result[::-1]