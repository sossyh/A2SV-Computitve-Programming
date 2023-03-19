class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows,cols = len(matrix), len(matrix[0])
        self.matrix = matrix
        self.prefixsum = [[0] * (cols + 1) for i in range((rows + 1))]
        
        
        for i in range(rows):
            for j in range(cols):
                self.prefixsum[i+1][j+1] = self.prefixsum[i][j+1] + self.prefixsum[i+1][j] - self.prefixsum[i][j] + matrix[i][j]
            
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefixsum[row2+1][col2+1] - self.prefixsum[row1][col2+1] - self.prefixsum[row2+1][col1] + self.prefixsum[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)