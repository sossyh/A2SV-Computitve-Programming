class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefixsum = []
        sums = 0
        d = {0:1}
        count = 0
        
        for i in nums:
            sums += i
            prefixsum.append(sums)
        
        for i in prefixsum:
            if (i - goal) in d:
                count += d[i - goal]
            if i not in d:
                d[i] = 0
            d[i] += 1
        print(d)
        
        return count
                