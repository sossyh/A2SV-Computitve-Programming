class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start = 0
        maxave = float("-inf")
        currsum = 0

        for end in range(len(nums)):
            currsum += nums[end]
            if end >= k - 1:
                maxave = max(maxave, currsum)
                currsum -= nums[start]
                start += 1
                
        return maxave/k
