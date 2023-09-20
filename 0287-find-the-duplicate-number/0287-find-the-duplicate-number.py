class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        visited = 0
        
        for i in nums:
            if visited & (1 << i):
                return i
            
            visited |= (1 << i)
                