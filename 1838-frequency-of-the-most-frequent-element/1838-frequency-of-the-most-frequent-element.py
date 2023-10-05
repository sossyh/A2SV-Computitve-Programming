class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        start = 0
        total = 0
        max_freq = 0
        
        for end in range(len(nums)):
            total += nums[end]
            
            while (nums[end] * (end - start + 1)) - total > k:
                total -= nums[start]
                start += 1
            
            max_freq = max(max_freq, end - start + 1)
            
        
        return max_freq