class Solution:
    def dp(self,idx, agescore, prevage, prevscore, memo):
        
            if idx in memo:
                return memo[idx]
            
            if idx >= len(agescore):
                return 0
            
            maxscore = 0
            
            for i in range(idx, len(agescore)):
                if not prevscore or (agescore[i][0] > prevage and agescore[i][1] >= prevscore) or (agescore[i][0] == prevage):      
                    a = self.dp(i+1, agescore, agescore[i][0], agescore[i][1], memo)
                    maxscore = max(maxscore, a + agescore[i][1])
            
            memo[idx] = maxscore
            return maxscore
        
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        agescore = [(ages[i], scores[i]) for i in range(len(scores))]
        agescore.sort()

        memo = {}            
        
        return self.dp(0, agescore, None, None, memo)
                