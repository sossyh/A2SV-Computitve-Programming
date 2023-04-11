class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = 0
        visited = set()
        graph = collections.defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j]:
                    graph[i+1].append(j+1)
        
        def dfs(vertex):
            nonlocal count
            if vertex in visited:
                return 0
            visited.add(vertex)
            for i in graph[vertex]:
                    dfs(i)
            return 1
        
        for i in graph:
            count += dfs(i)
        return count