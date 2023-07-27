class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        res = 1
        l, r = 0, 1
        length = 1
        
        while r < len(nums):
            if nums[l] < nums[r]:
                r += 1
                l += 1
                length += 1
            else:
                l = r
                r += 1
                length = 1
            
            res = max(res, length)
        
        return res

        