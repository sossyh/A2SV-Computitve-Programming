class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        def isinbound(r, c):
            return 0 <= r < n and 0 <= c < n
            
        n = len(grid)
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        
        
        
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        
        if n == 1:
            return 1
        
        queue = deque([(0,0,1)])

        while queue:

                item = queue.popleft()

                for i, j in directions:
                    newrow = item[0] + i
                    newcol = item[1] + j
                    if isinbound(newrow, newcol) and grid[newrow][newcol] == 0:
                        if newrow == n - 1 and newcol == n - 1:
                            return item[2] + 1
                        queue.append((newrow, newcol, item[2] + 1))
                        grid[newrow][newcol] = 1
        
        return -1