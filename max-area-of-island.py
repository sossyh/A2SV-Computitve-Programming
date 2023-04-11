class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        visited = set()
        count = 0
        marea = 0

        def isinbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        def dfs(row, col):
            nonlocal count
            if (row, col) in visited:
                return 0

            visited.add((row, col))
            count += 1

            for i, j in directions:
                newrow = row + i
                newcol = col + j
                if isinbound(newrow, newcol) and grid[newrow][newcol]:
                    dfs(newrow, newcol)

            return 1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    dfs(i,j)
                    marea = max(marea, count)
                    count = 0

        return marea