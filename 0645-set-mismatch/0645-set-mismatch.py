class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        result = []
        i = 0
        while i < len(nums):
            corr = nums[i] - 1
            if nums[corr] != nums[i]:
                nums[corr], nums[i] = nums[i], nums[corr]
            else:
                i += 1
        for i in range(len(nums)):
            if nums[i] != i + 1:
                result = [nums[i], i + 1]
                break
        return result
                