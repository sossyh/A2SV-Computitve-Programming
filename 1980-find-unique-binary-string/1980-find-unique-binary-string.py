class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        nums = set(nums)
        generated = set()
        
        
        def backtrack(idx, curr):
            if idx >= n:
                generated.add(curr)
                return
            
            backtrack(idx + 1, curr + "0")
            
            backtrack(idx + 1, curr + "1")
        
        
        backtrack(0, "")
        
        
        for i in generated:
            if i not in nums:
                return i
                
        