class Solution:
    def isinbound(self, r, c, n):
        return 0 <= r  < n and 0 <= c < n

    def shortestBridge(self, grid: List[List[int]]) -> int:
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        queue = deque()
        visited = set()
        n = len(grid)

        def dfs(row, col):
            visited.add((row, col))
            queue.append((row, col, 0))

            for i, j in directions:
                newr = row + i
                newc = col + j
                if self.isinbound(newr, newc, n) and (newr, newc) not in visited and grid[newr][newc] == 1:
                    dfs(newr, newc)
            
        a = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    a = 1
                    break
            if a == 1:
                break
        
    
        while queue:
            row, col, level = queue.popleft()
            for i, j in directions:
                newr = i + row
                newc = j + col
                if self.isinbound(newr, newc, n) and (newr, newc) not in visited:
                    if grid[newr][newc]:
                        return level
                    visited.add((newr, newc))
                    queue.append((newr, newc, level+1))