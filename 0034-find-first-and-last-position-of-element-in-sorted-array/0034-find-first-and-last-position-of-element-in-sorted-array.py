class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low, high = 0, len(nums)-1
        bestl = -1 
        bestr = -1
        a = bisect.bisect_left(nums, target)
        if a < len(nums) and nums[a] == target:
            bestl = a
        
        b = bisect.bisect_right(nums, target)
        print(b-1, len(nums))
        if (abs(b-1) < len(nums)) and nums[b-1] == target:
            bestr = b-1
        
        return [bestl, bestr]
        