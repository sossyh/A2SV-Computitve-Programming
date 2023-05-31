class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        directions = [(1,0), (0,1)]
        memo = {}
        count = 0

        def isinbound(row, col):
            return 0 <= row < m and 0 <= col < n

        def dfs(row, col):
            if row == m - 1 and col == n - 1:
                return 1       
                
            a = 0
            bottomr = row + 1
            bottomc = col + 0

            if isinbound(bottomr, bottomc):
                if (bottomr, bottomc) not in memo:
                    memo[(bottomr, bottomc)] = dfs(bottomr, bottomc)
                a = memo[(bottomr, bottomc)]
            
            b = 0
            rightr = row + 0
            rightc = col + 1
            if isinbound(rightr, rightc):
                if (rightr, rightc) not in memo:
                    memo[(rightr, rightc)] = dfs(rightr, rightc)
                b = memo[(rightr, rightc)]

            return a + b        

        return dfs(0, 0)