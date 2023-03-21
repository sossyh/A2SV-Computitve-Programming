class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        
        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
                
        for i in range(1,len(nums)):
            postfix[-1-i] = postfix[-1-(i-1)] * nums[-1-(i-1)]
        
        for i in range(len(nums)):
            result.append(prefix[i] * postfix[i])
        
        return result
        
            
            
        