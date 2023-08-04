class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        a1 = nums[0]
        a2 = nums[-1]
        
        if a1 > a2:
            for i in range(len(nums)-1):
                if nums[i] < nums[i+1]:
                    return False
        
        elif a1 < a2:
            for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    return False
            
        else:
            for i in range(1, len(nums)-1):
                if nums[i] != nums[i+1]:
                    return False
        
        return True