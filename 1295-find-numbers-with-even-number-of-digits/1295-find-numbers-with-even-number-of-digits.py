class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        
        for i in nums:
            digit = len(str(i))
            
            if digit % 2 == 0:
                count += 1
        
        return count
                
                