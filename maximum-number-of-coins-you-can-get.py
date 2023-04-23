class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        ans = 0
        l, r = 1, len(piles) - 1

        while l < r:
            ans += piles[l]
            l += 2
            r -= 1
        
        return ans