class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        
        isinbound = lambda r, c : 0 <= r < n and 0 <= c < n
        
        heap = []
        heappush(heap, (grid[0][0], (0, 0)))
        visited = set()
        
        while heap:
            curr_time, curr_place = heappop(heap)
            
            if curr_place[0] == n - 1 and curr_place[1] == n - 1:
                return curr_time
            
            if curr_place in visited:
                continue
                
            visited.add(curr_place)
            
            for i, j in directions:
                newr, newc = curr_place[0] + i, curr_place[1] + j
                
                if isinbound(newr, newc):
                    if grid[newr][newc] <= curr_time:
                        heappush(heap, (curr_time, (newr, newc)))
                    else:
                        diff = grid[newr][newc] - curr_time
                        heappush(heap, (curr_time + diff, (newr, newc)))