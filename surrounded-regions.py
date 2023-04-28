class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isInBound(r, c):
            return 0 <= r < len(board) and 0 <= c < len(board[0])

        visited = set()

        directions = [(0,1), (0,-1), (-1,0), (1,0)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if i == 0 or i == len(board) -1 or j == 0 or j == len(board[0])-1:
                    visited.add((i,j))

        def dfs(row, col):
            board[row][col] = 1
            for i, j in directions:
                newr = row + i
                newc = col + j
                if isInBound(newr, newc) and board[newr][newc] != 1 and board[newr][newc] == "O":
                    dfs(newr, newc)

        for i, j in visited:
            if board[i][j] == "O":
                dfs(i, j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if i == 0 or i == len(board) -1 or j == 0 or j == len(board[0])-1:
                    if board[i][j] == 1:
                        board[i][j] = "O"
                    continue
                     
                if board[i][j] == "O" and board[i][j] != 1:
                    board[i][j] = "X"
                
                if board[i][j] == 1:
                    board[i][j] = "O"