class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        
        for i, j, w in times:
            graph[i].append((j,w))
       
        min_time = -1
        visited = set()
        
        heap = []
        heappush(heap, (0, k))
        
        while heap:
            
            curr_time, curr_node = heappop(heap)
            
            if curr_node in visited:
                continue
            
            min_time = max(min_time, curr_time)
            
            visited.add(curr_node)
            
            for neighbour, weight in graph[curr_node]:
                heappush(heap, (curr_time + weight, neighbour))
        
        return min_time if len(visited) == n else -1
            
            