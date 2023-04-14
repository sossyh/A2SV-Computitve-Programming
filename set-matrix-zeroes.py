class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, col = [], []
        for i in range(len(matrix)):
            for k in range(len(matrix[0])):
                if matrix[i][k] == 0:
                    row.append(i)
                    col.append(k)
        
        for i in row:
            for k in range(len(matrix[0])):
                matrix[i][k] = 0

        for j in col:
            for k in range(len(matrix)):
                matrix[k][j] = 0