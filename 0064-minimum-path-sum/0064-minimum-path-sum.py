class Solution:
    def isinbound(self, row, col, m, n):
        return 0 <= row < m and 0 <= col < n
    
    def minPathSum(self, grid: List[List[int]]) -> int:
        directions = [(1,0), (0,1)]
        
        memo = {}
        
        def dp(row, col):
            if ((row, col)) in memo:
                return memo[(row, col)]
            
            if col == len(grid[0])-1 and row == len(grid)-1:
                return grid[row][col]
            
            call = inf
            for i, j in directions:
                newr = row + i
                newc = col + j
                if self.isinbound(newr, newc, len(grid), len(grid[0])):
                    a = dp(newr, newc)
                    call = min(call, a)
            
            memo[(row,col)] = grid[row][col] + call
            return grid[row][col] + call
        
        return dp(0,0)