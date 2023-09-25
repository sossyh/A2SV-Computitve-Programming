class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        agescore = [(ages[i], scores[i]) for i in range(len(scores))]
        agescore.sort()
        # print(agescore)
        memo = {}
        
        def dp(idx, prevage, prevscore):
            if idx in memo:
                return memo[idx]
            
            if idx >= len(scores):
                return 0
            
            maxscore = 0
            
            for i in range(idx, len(scores)):
                if not prevscore or (agescore[i][0] > prevage and agescore[i][1] >= prevscore) or (agescore[i][0] == prevage): 
                    
                    # if agescore[i][0] == prevage:
                        
                    a = dp(i+1, agescore[i][0], agescore[i][1])
                    maxscore = max(maxscore, a + agescore[i][1])
            
            memo[idx] = maxscore
            return maxscore
        
        return dp(0, None, None)
                