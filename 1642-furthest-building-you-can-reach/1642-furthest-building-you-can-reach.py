class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        n = len(heights)
        
        heap = []
        
        for i in range(n-1):
            diff = heights[i+1] - heights[i]
            
            if diff > 0 and ladders == 0 and (bricks == 0 or bricks < diff):
                return i
            
            if diff > 0:
                heapq.heappush(heap, -diff)
                bricks -= diff
                
                if bricks < 0:
                    ladders -= 1
                    bricks += -heapq.heappop(heap)
                
                        
        
        return len(heights) - 1
                
                