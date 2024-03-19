# https://leetcode.com/problems/n-ary-tree-preorder-traversal/

from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def dfs(root, output):
            if not root:
                return None
            output.append(root.val)
            for child in root.children:
                dfs(child, output)
            return output
        
        return dfs(root, [])
    

# Time: O(N)
# Space: O(N)
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.val)
            for child in reversed(node.children):
                stack.append(child)
                
        return result