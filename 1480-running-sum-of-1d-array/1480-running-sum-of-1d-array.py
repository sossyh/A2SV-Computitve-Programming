class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        sums = 0

        for i in nums:
            sums += i
            result.append(sums)
        
        return result