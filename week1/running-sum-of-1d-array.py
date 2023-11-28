class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefixsum = [nums[0]]

        for i in range(1, len(nums)):
            prefixsum.append(prefixsum[-1] + nums[i])
        
        return prefixsum