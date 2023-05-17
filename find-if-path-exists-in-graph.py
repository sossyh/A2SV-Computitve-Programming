class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(list)
        ans = collections.defaultdict(int)

        for i in edges:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])  
        visited = set()
        
        def dfs(vertex, parent):
            
            ans[vertex] = parent
            visited.add(vertex)
            
            for i in graph[vertex]:
                if i not in visited:
                    dfs(i, parent)
                        
        for i in range(n):
            if i not in visited:
                dfs(i, i)
            
        return ans[source] == ans[destination]