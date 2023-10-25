class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {}
        
        def backtracking(idx, sentence):
            if (idx, sentence) in memo:
                return memo[(idx, sentence)]
            
            if idx >= len(s):
                sentence = sentence[ : -1]
                return [sentence]
            
            
            curr_result = []
            for i in range(idx, len(s)):
                prefix = s[idx: i + 1]
                if prefix in wordDict:
                    inter_ans = backtracking(i + 1, sentence + prefix + " ")
                    curr_result.extend(inter_ans)
            
            memo[(idx, sentence)] = curr_result
            
            return curr_result
        
        return backtracking(0, "")
        
        
        
    
                        