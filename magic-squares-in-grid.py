class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
    
        def isdistinict(row, col):
            visited = set()
            for i in range(row - 1, row + 2):
                for j in range(col - 1, col + 2):
                    if 1 <= grid[i][j] <= 9:
                        visited.add(grid[i][j])
            
            return len(visited) == 9

        count = 0

        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[0]) - 1):
                if isdistinict(i, j):

                    rs = sum(grid[i - 1][j - 1: j + 2])
                    rows = sum(grid[i - 1][j - 1: j + 2]) == sum(grid[i][j - 1: j + 2]) == sum(grid[i + 1][j - 1: j + 2])
                    colums = rs == (grid[i-1][j-1] + grid[i][j-1] + grid[i+1][j-1]) == (grid[i-1][j] + grid[i][j] + grid[i+1][j]) == (grid[i-1][j+1] + grid[i][j+1] + grid[i+1][j+1]) 
                    diagonals = rs == (grid[i][j] + grid[i-1][j-1] + grid[i+1][j+1]) == (grid[i][j] + grid[i-1][j+1] + grid[i+1][j-1])
                
                    if rows and colums and diagonals:
                        count += 1
        
        return count