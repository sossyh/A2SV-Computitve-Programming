class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums = [i for i in range(1, n+1)]

        def helper(k, delidx):
            if len(nums) == 1:
                return nums[0]
            
            delidx = (delidx + k - 1) % len(nums)
            del nums[delidx]

            return helper(k, delidx)
        
        return helper(k, 0)