class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        visited = set()
        
        def backtrack(lst, idx):
            if len(lst) == len(nums):
                result.append(lst[:])
                return
            
            for i in range(len(nums)):
                if nums[i] not in visited:
                    
                    lst.append(nums[i])
                    visited.add(nums[i])
                    
                    backtrack(lst, i + 1)
                    
                    lst.pop()
                    visited.remove(nums[i])
                    
        
        backtrack([], 0)
        
        return result
        