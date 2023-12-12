class Solution:
    def is_in_bound(self, r, c, m, n):
        return 0 <= r < m and 0 <= c < n

    def dfs(self, row, col, grid, visited):
        visited.add((row, col))

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for i, j in directions:
            new_r = row + i
            new_c = col + j

            if self.is_in_bound(new_r, new_c, len(grid), len(grid[0])) and (new_r, new_c) not in visited and grid[new_r][new_c] == "1":
                self.dfs(new_r, new_c, grid, visited)

            
        
    def numIslands(self, grid: List[List[str]]) -> int:
       """
       proble: find the number of islands

       solution: 1. plan to use dfs
                 2. starting form any "1"'s and do the dfs given the 4 directions
                 3. increase count when the dfs ends
                 4. repeat from #2 and #3 until all cells are visited
        
        
       complexty anlysis:
        TC: O(4 + N * M) - O(N * M)
        SC: O(N * M)       
       
       """

       count = 0
       visited = set()

       for i in range(len(grid)):
           for j in range(len(grid[0])):
               if grid[i][j] == '1' and (i, j) not in visited:
                   self.dfs(i, j, grid, visited)
                   count += 1
        
       return count


