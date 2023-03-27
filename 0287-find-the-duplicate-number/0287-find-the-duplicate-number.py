class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            corr = nums[i] - 1
            if nums[i] != nums[corr]:
                nums[i], nums[corr] = nums[corr], nums[i]
            else:
                i += 1
        
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return nums[i]
                
                