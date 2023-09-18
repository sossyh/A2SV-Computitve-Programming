class Solution:
    def isinbound(self, row, col, n):
        return 0 <= row < n and 0 <= col < n
    
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        directions = [-1, 0, 1]
        
        @cache
        def dp(row, col):
            if row == len(matrix)-1:
                return matrix[row][col]
            
            minn = inf
            
            for i in directions:
                if self.isinbound(row+1, col+i, len(matrix)):
                    a = dp(row+1, col+i)
                    minn = min(minn, a)
            
            return minn + matrix[row][col]
        
        
        ans = inf
        for i in range(len(matrix[0])):
            
            a = dp(0,i)
            ans = min(ans, a)
        
                       
        return ans
            
            
            