class Solution:
    def reverse(self, s):
        lst = list(s)
        l, r =0, len(lst) - 1
        while l < r:
            lst[l], lst[r] = lst[r], lst[l]
            l += 1
            r -= 1
        return "".join(lst)
            
    def invert(self, s):
        ans = ""
        for i in s:
            if i == '0':
                ans += '1'
            else:
                ans += '0'
        return ans
    
        
    def findKthBit(self, n: int, k: int) -> str:
        
        def former(n):
            if n == 1:
                return "0"
            ans = former(n - 1)
            inverted = self.invert(ans)
            rever = self.reverse(inverted)
            return ans + "1" + rever
        
        res = former(n)
        return res[k - 1]