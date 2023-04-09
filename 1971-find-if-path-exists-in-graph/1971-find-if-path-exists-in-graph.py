class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(list)
        
        for i in edges:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])  
        visited = set()
        
        def dfs(vertex):
            
            if vertex == destination:
                return True
            if graph[vertex] == []:
                return False
            visited.add(vertex)
            
            for i in range(len(graph[vertex])):
                
                if graph[vertex][i] not in visited:
                    if dfs(graph[vertex][i]):
                        return True
        
        return dfs(source)
                
            
            