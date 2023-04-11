class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.n = len(graph)
        result = []
        g = defaultdict(list)
        for i in range(len(graph)):
            g[i] += (graph[i])
        
        def dfs(lst, vertex):
            if vertex == self.n - 1:
                result.append(lst[:])
                return
            for i in g[vertex]:
                lst.append(i)
                dfs(lst, i)
                lst.pop()
        
        dfs([0], 0)
        return result