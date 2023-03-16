class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(candidates)
        
        def backtrack(lst, cadsum, idx):
            if cadsum == target:
                result.append(lst[:])
                return
            if cadsum > target or idx >= n:
                idx += 1
                return
            
            lst.append(candidates[idx])
            backtrack(lst, cadsum + candidates[idx] , idx)
            
            lst.pop()
            backtrack(lst, cadsum, idx + 1)
        
        backtrack([], 0, 0)            
            
        return result
                
                
            