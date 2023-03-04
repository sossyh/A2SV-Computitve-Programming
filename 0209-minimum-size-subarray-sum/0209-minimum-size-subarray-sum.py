class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        minL = float("inf")
        currSum = 0
        
        for end in range(len(nums)):
            currSum += nums[end]
            while currSum >= target:
                minL = min(minL, end - start + 1)
                currSum -= nums[start]
                start += 1
        
        return minL if minL != float("inf") else 0