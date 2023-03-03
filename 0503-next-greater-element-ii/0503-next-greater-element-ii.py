class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1]*n
        stack = []
        
        for i in range(2*n):
            
            while stack and nums[stack[-1]] < nums[i % n]:
                idx = stack.pop()
                val = nums[idx]
                result[idx] = nums[i % n]
            stack.append(i % n)
            
        return result
        