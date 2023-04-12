class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        startingcolor = image[sr][sc]
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = set()

        def isinbound(row, col):
            return 0 <= row < len(image) and 0 <= col < len(image[0])
        
        def dfs(row, col):
            if (row, col) in visited:
                return

            image[row][col] = color
            visited.add((row, col))

            for i, j in directions:
                newrow = row + i
                newcol = col + j
                if isinbound(newrow, newcol) and image[newrow][newcol] == startingcolor:
                    dfs(newrow, newcol)
        
        dfs(sr, sc)

        return image