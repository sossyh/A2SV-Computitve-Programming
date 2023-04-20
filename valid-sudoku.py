class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        visitedRow = collections.defaultdict(set)
        visitedCol = collections.defaultdict(set)

        for i in range(len(board)): 
            for j in range(len(board[0])):
                if i % 3 == 0 and j % 3 == 0:
                    visitedcells = set()
                
                    for  k in range(i,i+3):
                        for m in range(j, j+3):
                            if board[k][m] == ".":
                                continue

                            if int(board[k][m]) in visitedcells:
                                return False
                            
                            visitedcells.add(int(board[k][m]))
                            

                if board[i][j] == ".":
                    continue


                if int(board[i][j]) in visitedCol[j] or int(board[i][j]) in visitedRow[i]:
                    return False

                visitedRow[i].add(int(board[i][j]))
                visitedCol[j].add(int(board[i][j]))
                        
        return True