class Solution:
    def findPeek(self, nums):
        # chars pick both the left and right elets are less than the pick
        low, high = 0, len(nums) - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if mid == 0:
                if len(nums) == 1 or nums[mid] > nums[mid + 1]:
                    return 0
            
            if mid == len(nums) - 1:
                return mid
            
            if nums[mid] > nums[mid + 1]:
                return mid
            
            elif nums[mid] >= nums[0]:
                low = mid + 1
            
            else:
                high = mid - 1
                              
    def search(self, nums: List[int], target: int) -> int:
        peek = self.findPeek(nums)
        # print(peek)
        if target == nums[peek]:
            return peek
        
        low, high = 0, peek - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                low = mid + 1
            
            else:
                high = mid - 1
        
        
        low, high = peek + 1, len(nums) - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                low = mid + 1
            
            else:
                high = mid - 1
        
        return -1
        