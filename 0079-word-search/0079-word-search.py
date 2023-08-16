class Solution:
    def isinbound(self, r, c, m, n):
        return 0 <= r < m and 0 <= c < n
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(1,0), (-1, 0), (0,1), (0,-1)]
        rowlen, collen = len(board), len(board[0])
        
        def backtrack(idx, row, col):
            if idx == len(word):
                return True
            
            visited.add((row,col))
            for i, j in directions:
                newr = row + i
                newc = col + j
                
                if (newr,newc) not in visited and self.isinbound(newr, newc, rowlen, collen) and word[idx] == board[newr][newc]:
                    
                    if backtrack(idx+1, newr, newc):
                        return True
                    visited.remove((newr, newc))
        
        
        for i in range(rowlen):
            for j in range(collen):
                if board[i][j] == word[0]:
                    visited = set()
                    if backtrack(1, i, j):
                        return True
                    
            