class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        if len(nums) == 2:
            return max(nums[1], nums[0])

        n = len(nums)
        memo = {}

        def helper(i):
            if i == 0:
                return nums[i]
            
            if i == 1:
                return max(nums[1], nums[0])
            
            if i not in memo:
                a = helper(i-1)
                b = helper(i-2) + nums[i]
                memo[i] = max(a, b)
        
            return memo[i]
        
        ans1 = helper(n-2)
        nums = nums[1:]

        memo = {}
        ans2 = helper(n-2)
        print(ans1, ans2)

        return  max(ans1, ans2)