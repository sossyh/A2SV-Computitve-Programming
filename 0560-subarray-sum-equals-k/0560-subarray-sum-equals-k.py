class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        d = {0:1}
        
        sums = 0
        for i in nums:
            sums += i
            if (sums - k) in d:
                count += d[sums - k]
            if sums not in d:
                d[sums] = 0
            d[sums] += 1
        
        return count