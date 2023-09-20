class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        memo = {}
        
        def dp(idx, lst):
            if idx in memo:
                return memo[idx]
            
            if idx >= len(nums):
                return 0
            
            ans = 0
            
            for i in range(idx, len(nums)):
                if len(lst) < 1 or (len(lst) == 1 and lst[0] != nums[i])  or ( len(lst) >= 2 and lst[-1] - lst[-2] > 0 and nums[i] - lst[-1] < 0) or (len(lst) >= 2 and lst[-1] - lst[-2] < 0 and nums[i] - lst[-1] > 0):
                    
                        
                    lst.append(nums[i])
                    
                    a = dp(i+1, lst)
                    ans = max(ans, a+1)
                    
                    lst.pop()
            
            memo[idx] = ans
            
            return ans
        
        return dp(0, [])
                