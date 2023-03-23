class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = {}
        
        for i in range(len(nums)+1):
            if nums[i] not in d:
                d[nums[i]] = 0
            else:
                return nums[i]
        