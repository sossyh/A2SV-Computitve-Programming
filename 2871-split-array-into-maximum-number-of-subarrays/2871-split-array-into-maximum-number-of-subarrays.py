class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        all_and = nums[0]
        
        for i in nums:
            all_and &= i
        
        if all_and > 0:
            return 1
        
        count = 0
        curr = pow(2, 32) - 1
        
        for i in range(len(nums)):
            curr &= nums[i]
            
            if curr == 0:
                count += 1
                curr = pow(2, 32) - 1
                
        return count
            