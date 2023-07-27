class Solution:
    def isinbound(self, row, col, grid):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        count = 0

        
        def dfs(row, col):
            visited.add((row, col))
            
            ans = None
            
            final = True
            for k, l in directions:
                i, j = row+k, col+l
                if (i, j) not in visited and self.isinbound(i, j, grid2) and grid2[i][j] == 1:
                    if not dfs(i, j):
                        final = False

            
            if grid1[row][col] == 1:
                ans = final
            else:
                ans = False
            return ans
        
        
        visited = set()
        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                if grid2[i][j] == 1 and (i,j) not in visited:
                    if dfs(i,j):
                        count += 1
                
                    
        return count
                    
                