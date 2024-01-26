class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        @cache
        def dp(row, col, maxmove):
            if maxmove < 0:
                return 0

            if row < 0 or col < 0 or row >= m or col >= n:
                return 1
            
            total = 0

            for i, j in directions:
                total += dp(row + i, col + j, maxmove - 1)
            
            return total % (pow(10, 9) + 7)
        
        return dp(startRow, startColumn, maxMove)