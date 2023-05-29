class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = [-1 for i in range(n+1)]

        def dp(i):
            if i == 0:
                nums[i] = 0
                return nums[i]
            if i == 1:
                nums[i] = 1
                return nums[i]
            
            if nums[i] == -1:
                if i % 2 == 1:
                    nums[i] = dp(i//2) + dp(i//2 + 1)
                else:
                    nums[i] = dp(i//2)
            
            return nums[i]

        # ans = float("-inf")
        for i in range(len(nums)):
            if nums[i] == -1:
                dp(i)

        return max(nums)