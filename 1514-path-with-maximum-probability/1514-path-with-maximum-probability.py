class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        
        for i in range(len(edges)):
            u, v, w = edges[i][0], edges[i][1], succProb[i]
            graph[u].append((v, w))
            graph[v].append((u, w))
            
        distance = [0 for i in range(n)]
        distance[start_node] = 0
        
        heap = []
        heappush(heap, (-1, start_node))
        visited = set()
        
        while heap:
            curr_probability, curr_node = heappop(heap)
            
            if curr_node in visited:
                continue
            
            visited.add(curr_node)
            
            if curr_node == end_node:
                return abs(curr_probability)
            
            for nbr, w in graph[curr_node]:
                new_probility = abs(curr_probability) * w
                heappush(heap, (-new_probility, nbr))
        
        return 0
                
            