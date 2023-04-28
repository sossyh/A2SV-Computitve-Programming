class Solution:
    def isInBound(self, grid, r, c):
        return 0 <= r < len(grid) and 0 <= c < len(grid[0])

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        result = mat.copy()
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        queue =deque()
        visited = set()

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]  == 0:
                    visited.add((i,j))
                    queue.append((i, j, 0))
        
        while queue:
            item = queue.popleft()
            for i, j in directions:
                newr = item[0] + i
                newc =  item[1] + j
                if self.isInBound(mat, newr, newc) and (newr,newc) not in visited:
                    visited.add((newr, newc))
                    queue.append((newr, newc, item[2] + 1))
                    result[newr][newc] = item[2] + 1

        return result