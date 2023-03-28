class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums) + 2
        
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = n
        
        for j in range(len(nums)):
            if abs(nums[j]) > 0 and abs(nums[j]) <= len(nums):
                idx = abs(nums[j]) - 1
                nums[idx] = - abs(nums[idx])
        
        for k in range(len(nums)):
            if nums[k] > 0:
                return k + 1
            
        return len(nums) + 1
                