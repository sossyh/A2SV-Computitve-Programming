class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        if len(nums) == 1:
            return [nums[:]]
        
        for i in range(len(nums)):
            first = nums.pop(0)
            resultinter = self.permute(nums)
            
            for i in range(len(resultinter)):
                resultinter[i].append(first)
            
            result += resultinter
            nums.append(first)
            
        return result
        