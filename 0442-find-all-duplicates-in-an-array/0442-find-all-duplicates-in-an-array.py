class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        i = 0
        
        while i < len(nums):
            rightposition = nums[i] - 1 
            if nums[i] != nums[rightposition]:
                nums[rightposition], nums[i] = nums[i], nums[rightposition]
            else:
                i += 1
        
        for i in range(len(nums)):
            if nums[i] != i + 1:
                result.append(nums[i])
        
        return result