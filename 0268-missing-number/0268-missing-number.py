class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        
        while i < len(nums):
            if nums[i] < i and i != nums[i]:
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
            else:
                i += 1
            
        for i in range(len(nums)):
            if i != nums[i]:
                return i
            
        return len(nums)
            
            