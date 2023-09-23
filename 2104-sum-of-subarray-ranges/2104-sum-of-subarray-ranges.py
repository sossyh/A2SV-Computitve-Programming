class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        nums.append(-inf)
        smallsums = 0
        stack = []
        
        for i in range(len(nums)):
            currlb = i - 1
            
            while stack and nums[stack[-1][1]] > nums[i]:
                val = stack.pop()
                leftspan = val[1] - val[0]
                rightspan = i - val[1]
                freq = leftspan * rightspan
                
                smallsums += freq * nums[val[1]]
                currlb = val[0]
                
                
            stack.append((currlb, i))
        
        nums.pop()
        nums.append(inf)
        stack = []
        largesums = 0
        
        for i in range(len(nums)):
            
            currlb = i - 1
            
            while stack and nums[stack[-1][1]] < nums[i]:
                val = stack.pop()
                leftspan = val[1] - val[0]
                rightspan = i - val[1]
                freq = leftspan * rightspan
                
                largesums += freq * nums[val[1]]
                currlb = val[0]
            
            stack.append((currlb, i))
        
        return largesums - smallsums
            
        