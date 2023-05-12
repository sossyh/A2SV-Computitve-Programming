class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        result = [None for i in range(n)]
        graph = defaultdict(list)
        
        for i, j in richer:
            graph[j].append(i)
    
        def dfs(vertex):
            if graph[vertex] == []:
                result[vertex] = vertex
                return
            
            low = vertex
            for i in graph[vertex]:
                if result[i] == None:
                    dfs(i)
                low = low if quiet[low] < quiet[result[i]] else result[i]
            
            result[vertex] =low
            
        for i in range(n):
            if result[i] == None:
                dfs(i)
        
        return result