class Solution:
    def bisect_left(self, nums, target):
        l, r = 0, len(nums) - 1
        best = len(nums)

        while l <= r:
            mid = l + (r - l) // 2
            if target <= nums[mid]:
                best = mid
                r = mid - 1
            else:
                l = mid + 1

        return best
    
        
        
    def bisect_right(self, nums, target):
        l, r = 0, len(nums) - 1
        best = len(nums)

        while l <= r:
            mid = l + (r - l) // 2

            if target >= nums[mid]:
                best = mid
                l = mid + 1
            else:
                r = mid - 1

        return best + 1
        
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low, high = 0, len(nums)-1
        bestl = -1 
        bestr = -1
        a = self.bisect_left(nums, target)
        if a < len(nums) and nums[a] == target:
            bestl = a
        
        b = self.bisect_right(nums, target)
        
        if (abs(b-1) < len(nums)) and nums[b-1] == target:
            bestr = b-1
        
        return [bestl, bestr]
        