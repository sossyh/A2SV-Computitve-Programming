class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        
        def backTrack(lst, num):
            if len(lst) == k:
                result.append(lst.copy())
                return
            for i in range(num, n+1):
                # appending candidates
                lst.append(i)
                # backtarcking
                backTrack(lst, i+1)
                
                lst.pop()
        
        backTrack([], 1)
        
        return result
                
                
            
        
        
        