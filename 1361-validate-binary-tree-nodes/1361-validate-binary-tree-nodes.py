class Solution:
    def check_disconnected(self, node, graph, n):
        queue = deque([node])
        visited = set()
        
        while queue:
            curr = queue.popleft()
            visited.add(curr)
            
            for child in graph[curr]:
                queue.append(child)
        
        if len(visited) != n:
            return False
        
        return True
    
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parent = defaultdict(list)
        graph = defaultdict(list)
        
        for i in range(n):
            if leftChild[i] != -1:
                graph[i].append(leftChild[i])
            if rightChild[i] != -1:
                graph[i].append(rightChild[i])
        
        for i in range(n):
            if leftChild[i] != -1:
                parent[leftChild[i]].append(i)
            
            if rightChild[i] != -1:
                parent[rightChild[i]].append(i)
        
        countNoneParent = 0
        nodewithnone = None
        
        for i in range(n):
            if parent[i] == []:
                countNoneParent += 1
                nodewithnone = i
                
        
        if countNoneParent != 1:
            return False
        
        for i in range(n):
            if i != nodewithnone and len(parent[i]) != 1:
                return False
        
        return self.check_disconnected(nodewithnone, graph, n)
        
        