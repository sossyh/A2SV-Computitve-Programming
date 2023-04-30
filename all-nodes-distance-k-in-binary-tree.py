# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildgraph(self, root, parent = None):
        if not root:
            return

        if parent != None:
            self.graph[root.val].append(parent)

        if root.left:
            self.graph[root.val].append(root.left.val)
        if root.right:
            self.graph[root.val].append(root.right.val)
        self.buildgraph(root.left, root.val)
        self.buildgraph(root.right, root.val)

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if k == 0:
            return [target.val]

        self.graph = defaultdict(list)
        self.buildgraph(root)
        print(self.graph)
        queue = deque()
        queue.append((target.val,0))
        visited = set()
        visited.add(target.val)
        result = []

        while queue:
            item = queue.popleft()
            
            if item[1] > k:
                break
           
            for i in self.graph[item[0]]:
                
                if i not in visited:

                    if item[1] + 1 == k:
                        result.append(i)

                    queue.append((i,item[1] + 1))
                    visited.add(i)
            
        return result