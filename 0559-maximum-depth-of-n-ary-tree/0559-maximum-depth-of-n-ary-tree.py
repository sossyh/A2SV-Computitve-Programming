"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        count = 0
        
        def bfs(root):
            nonlocal count
            queue = deque()
            queue.append(root)
            
            while queue:
                count += 1
                for i in range(len(queue)):
                    ans = queue.popleft()
                    for child in ans.children:
                        queue.append(child)
        
        bfs(root)
        return count