class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        for i in range(len(tasks)):
            tasks[i].append(i)
            
        result = []
        heap = []
        tasks.sort(key = lambda x:x[0])
        time = tasks[0][0]
        i = 0
        
        while heap or  i < (len(tasks)):
            
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(heap, (tasks[i][1], tasks[i][2]))
                i += 1
            
            if not heap and i < len(tasks):
                time = tasks[i][0]
                
            if heap:
                item = heapq.heappop(heap)
                result.append(item[1])
                time += item[0]
        
        
        
        
        return result
