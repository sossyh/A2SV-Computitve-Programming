class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        visited = set()
        result = []
        
        def backtrack(lst, candsum, idx):
            
            if candsum == target:
                result.append(lst[:])
                return
            
            if idx >= len(candidates):
                return
            
            if candsum > target:
                return
            
            for i in range(idx, len(candidates)):
                                 
                if i > idx and candidates[i] == candidates[i-1]:
                        continue
                lst.append(candidates[i])
                candsum += candidates[i]

                backtrack(lst, candsum, i + 1)
                
                back = lst.pop()
                candsum -= back
                    
        
        candidates.sort()
        
        backtrack([], 0, 0)
        
        return result
                