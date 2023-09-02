class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1]*n
        stack = []
        
        for i in range(2*n):
            while stack and nums[i%n] > nums[stack[-1]]:
                idx = stack.pop()
                result[idx] = nums[i%n]
            
            stack.append(i%n)
        
        return result