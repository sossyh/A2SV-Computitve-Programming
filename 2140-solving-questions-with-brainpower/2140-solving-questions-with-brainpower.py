class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        
        @cache
        def backtrack(idx):
            if idx == n - 1:
                return questions[n-1][0]
            
            if idx >= n:
                return 0
            
            newi = idx + questions[idx][1] + 1
            ans1 = backtrack(newi) + questions[idx][0]
            ans2 = backtrack(idx + 1)
            
            return max(ans1, ans2)
        
        return backtrack(0)
            
            

            
            