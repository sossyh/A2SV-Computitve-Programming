class Solution:
    def countOdds(self, low: int, high: int) -> int:
        ans = high - low + 1
        
        if ans % 2 == 0:
            return ans // 2
        else:
            if low % 2 == 1:
                return (ans//2) + 1
            else:
                return ans//2