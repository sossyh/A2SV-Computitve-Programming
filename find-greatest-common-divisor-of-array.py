class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mn = nums[0]
        mx = nums[0]
        ans = 1
        for i in nums:
            mn = min(mn, i)
            mx = max(mx, i)
        for i in range(mn,0,-1):
            if mx%i == 0 and mn % i == 0:
                ans = i
                break
        
        return ans