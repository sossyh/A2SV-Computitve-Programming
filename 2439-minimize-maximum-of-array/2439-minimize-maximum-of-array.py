class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        result = nums[0]
        summ = nums[0]
        
        for i in range(1, len(nums)):
            summ += nums[i]
            ave = math.ceil(summ / (i+1))
            
            
            result = max(result, ave)
        
        return result