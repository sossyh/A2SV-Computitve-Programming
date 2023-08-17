class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        
        dp = [0] * n
        
        for i in range(n-1, -1, -1):
            considernext = dp[i+1] if i < (n-1) else 0
            
            considercurrent = questions[i][0] + (dp[(questions[i][1]+1+i)] if (questions[i][1]+1+i) < n else 0)
            
            dp[i] = max(considernext, considercurrent)
        
        return dp[0]
            

            
            