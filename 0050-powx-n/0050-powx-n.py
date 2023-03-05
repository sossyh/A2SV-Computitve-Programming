class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        
        def helper(num, power):
            if power == 0:
                return 1
            res = helper(num * num, power//2)
            return res if power%2 == 0 else num * res
        
        ans = helper(x, abs(n))
        
        return ans if n >= 0 else 1/ ans
        
            
            
