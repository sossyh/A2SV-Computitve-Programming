class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i]*2
                nums[i+1] = 0
        
        w = 0
        for r in range(len(nums)):
            if nums[r]:
                nums[w], nums[r] = nums[r], nums[w]
                w += 1
        
        return nums
            