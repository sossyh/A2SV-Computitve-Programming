class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        used = 0
        
        def backtrack(lst, idx):
            nonlocal used
            
            if len(lst) == len(nums):
                result.append(lst[:])
                return
            
            for i in range(len(nums)):
                if not (used & (1 << i)):
                    lst.append(nums[i])
                    used |= (1 << i)
                    
                    backtrack(lst, idx + 1)
                    
                    lst.pop()
                    used &= ~(1 << i)
            
            
            
            
        backtrack([], 0)
        
        return result
        