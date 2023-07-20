class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        prefixsum = []
        ans = []
        summ = 0
        
        for i in nums:
            summ += i
            prefixsum.append(summ)
        
        for i in range(len(nums)):
            leftsum = prefixsum[i-1] if i > 0 else 0
            rightsum = prefixsum[-1] - prefixsum[i]
            ans.append(abs(rightsum - leftsum))
        
        return ans            