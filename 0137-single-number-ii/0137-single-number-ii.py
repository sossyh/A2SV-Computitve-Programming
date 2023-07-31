class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0

        for i in range(32):
            c = 0
            for num in nums:
                if num < 0:
                    num = num & (2**32-1)
                c += (num >> i) & 1
                
            c %= 3
            ans |= c << i

        
        if ans >= 2**31:
            ans -= 2**32

        return ans