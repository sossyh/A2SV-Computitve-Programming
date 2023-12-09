class Solution:
    def maxStrength(self, nums: List[int]) -> int:  
        self.max = -inf

        def backtracking(idx, curr_prod, count):
            if idx >= len(nums):
                if count != 0:
                    self.max = max(self.max, curr_prod)
                return 
            
            pick = backtracking(idx + 1, curr_prod * nums[idx], count + 1)

            dont_pick = backtracking(idx + 1, curr_prod, count)
        
        backtracking(0, 1, 0)

        return self.max 

        [0] - [-1] - 0   - [-1]
        [0] - [0] - 0     - [1]


            
        
        # exploring every combination
        # calculating the maximun

"""
        [0, -1]

        [3,-1,-5,2,5,-9]
        [3], [-1], ........
        [3, -1], [3, -5], [-1, -5] ................
        [3, -1, -5] ........

        n = len(nums)

        [3]   ------- ------- 1
    / /   |  \   \
[-1] [-5] [2] [5] [-9] -------- 1 * n - 1
                       --------- (n- 1) * (n - 2)
                       --------- (n - 1) * (n - 2) * (n - 3)


                       --------- (n - 1) * (n - 2) ------ * (2) * (1)

total time complexty = (n - 1) * (n - 2) ------ * (2) * (1)) + (n - 1) * (n - 2) * (n - 3)
n! + n - 1! + n - 2! .................
the ass time = n!

space = o(n)
"""

# state - idx, curr_prod
# the base case -- if idx >= len(nums)
# will call with all of the numbers in the arr
   



