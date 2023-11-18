class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        
        i, j = 0, len(nums) - 1
        
        ans = -inf
        
        while i < j:
            inter = nums[i] + nums[j]
            ans = max(ans, inter)
            i += 1
            j -= 1
        
        return ans
        