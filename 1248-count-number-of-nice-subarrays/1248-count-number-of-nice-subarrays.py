class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                nums[i] = 1
            else:
                nums[i] = 0
        
        count = 0
        sums = 0
        d = {0:1}
        
        for i in nums:
            sums += i
            if sums - k in d:
                count += d[sums - k]
            if sums not in d:
                d[sums] = 0
            d[sums] += 1
        
        
        return count