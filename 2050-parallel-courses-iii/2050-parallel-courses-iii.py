class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        incoming = [0 for i in range(n)]
        
        for i, j in relations:
            graph[i - 1].append(j - 1)
            incoming[j - 1] += 1
        
        total_time = 0
        queue = []
        
        for i in range(n):
            if incoming[i] == 0:
                heappush(queue, (time[i], i))
        
        while queue:
            level_time = 0
            for i in range(len(queue)):
                curr_time, node = heappop(queue)
                level_time = max(curr_time, level_time)
                
                for nbr in graph[node]:
                    incoming[nbr] -= 1
                    if incoming[nbr] == 0:
                        
                        time[nbr] += level_time
                        heappush(queue, (time[nbr], nbr))
            
            
            total_time = level_time
        
        
        return total_time
        