class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        visited = set()
        self.perimeter = 0
        
        def isinbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        
        def dfs(row, col):
            if (row, col) in visited:
                return 
            
            if not isinbound(row, col) or grid[row][col] == 0:
                self.perimeter += 1
                return
                
            visited.add((row,col))
            for i, j in directions:
                newrow = row + i
                newcol = col + j
                dfs(newrow, newcol)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    dfs(i,j)
        
        return self.perimeter
        
            