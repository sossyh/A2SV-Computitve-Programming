class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        graph = defaultdict(list)
        
        
        for i, j in paths:
            graph[i].append(j)
            
        
        for k, l in paths:
            if graph[k] == []:
                return k
            if graph[l] == []:
                return l