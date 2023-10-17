class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        min_elet = min(nums)
        max_elet = max(nums)
        min_range = (max_elet - k) - (min_elet + k)
        
        if min_range <= 0:
            return 0
        return min_range