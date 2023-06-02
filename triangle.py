class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = defaultdict(int)
        

        def dynamic(row, col):
            if row == len(triangle) - 1:
                return (triangle[row][col])
            
            state = (row, col)
            if state not in dp:
                dp[state] = triangle[row][col] + min(dynamic(row+1, col), dynamic(row+1, col+1))
            
            return dp[state]
        
        
        return dynamic(0, 0)