class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        # nums = [i+1 for i in range(n)]
        
        def backTrack(lst, idx):   
            if idx >= n:
                if len(lst) == k:
                    result.append(lst[:])
                return
           
            lst.append(idx+1)
            backTrack(lst, idx+1)   
            lst.pop()
            backTrack(lst, idx+1)
        
        backTrack([], 0)
        
        return result
                
                
            
        
        
        