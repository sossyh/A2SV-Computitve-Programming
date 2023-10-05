class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n = len(dungeon)
        m = len(dungeon[0])
        
        dp = [[0 for i in range(m+1)] for j in range(n+1)]
        
        dp[n-1][m-1] = dungeon[n-1][m-1]
        
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                value = 0
                if j == m - 1:
                    value = dp[i+1][j] + + dungeon[i][j]
                elif i == n - 1:
                    value = dp[i][j+1] + + dungeon[i][j]
                else:
                    value = max(dp[i][j+1], dp[i+1][j]) + dungeon[i][j]
                
                dp[i][j] = value if value <= 0 else 0
                
        
        return abs(dp[0][0]) + 1
                
            