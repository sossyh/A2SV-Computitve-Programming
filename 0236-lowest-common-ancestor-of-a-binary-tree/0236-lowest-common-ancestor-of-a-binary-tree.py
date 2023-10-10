# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution: 
    def build_tree_graph(self, root):
        tree_graph = defaultdict(int)
        
        queue = deque()
        queue.append(root)
        
        while queue:
            curr = queue.popleft()
            
            if curr.left:
                tree_graph[curr.left.val] = (curr.val)
                queue.append(curr.left)
            
            if curr.right:
                tree_graph[curr.right.val] = (curr.val)
                queue.append(curr.right)
        
        return tree_graph       
    
    def dfs_traversal(self, tree, node):
        if node not in tree:
            return [node]
        
        result = self.dfs_traversal(tree, tree[node])
        result.append(node)
        
        return result
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        g_tree = self.build_tree_graph(root)
        
        ancestors_p = self.dfs_traversal(g_tree, p.val)
       
        ancestors_q =  self.dfs_traversal(g_tree, q.val)
        
        prev = None
        
        for i in range(min(len(ancestors_p), len(ancestors_q))):
            if ancestors_p[i] != ancestors_q[i]:
                break
            prev = ancestors_p[i]
        
        return TreeNode(prev)
        
        
        
        
        
        
        