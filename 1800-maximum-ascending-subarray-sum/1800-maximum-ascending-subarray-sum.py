class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxsum = nums[0]
        curr = nums[0]
        i, j = 0, 1
        
        while j < len(nums):
            if nums[j] > nums[i]:
                curr += nums[j]
                i += 1
                j += 1
            else:
                curr = nums[j]
                i = j
                j += 1
            
            maxsum = max(maxsum, curr)
        
        return maxsum
            