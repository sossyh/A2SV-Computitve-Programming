class Solution:
    def dfs(self, node, graph, visited):
        visited.add(node)
        self.result.append(node)
        
        for nbr in graph[node]:
            if nbr not in visited:
                self.dfs(nbr, graph, visited)
        
        
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        for i, j in adjacentPairs:
            graph[i].append(j)
            graph[j].append(i)
        
        self.result = []
        
        for i in graph:
            if len(graph[i]) == 1:
                self.dfs(i, graph, visited = set())
                break
        
        return self.result
        
    