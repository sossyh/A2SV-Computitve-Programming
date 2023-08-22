class Solution:
    def isinbound(self, r, c, m, n):
        return 0 <= r < m and 0 <= c < n
    
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        directions = [(0,1), (0,-1), (1,0), (-1,0), (-1,-1), (-1,1), (1,-1), (1,1)]
        m, n = len(board), len(board[0])
        visited = set()
        
        def dfs(row, col):
            if board[row][col] == "M":
                board[row][col] = 'X'
                return
            
            visited.add((row, col))
            
            adjminerevealed = False
            
            for i, j in directions:
                newr = row + i
                newc = col + j
                if self.isinbound(newr, newc, m, n) and (board[newr][newc] == 'X' or board[newr][newc] == 'M'):
                    adjminerevealed = True
            
            if not adjminerevealed:
                board[row][col] = 'B'
                
                for i, j in directions:
                    newr = row + i
                    newc = col + j
                    if (newr, newc) not in visited and self.isinbound(newr, newc, m, n):
                        dfs(newr, newc)
            
            else:
                minecount = 0
                for i, j in directions:
                    newr = row + i
                    newc = col + j
                    if self.isinbound(newr, newc, m, n) and (board[newr][newc] == 'X' or board[newr][newc] == 'M'):
                        minecount += 1
                
                board[row][col] = str(minecount)
                  
                         
        dfs(click[0], click[1])
        
        return board