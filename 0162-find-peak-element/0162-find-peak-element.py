class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        low, high = 0, len(nums) - 1
    
        while low <= high:
            mid = low + (high - low) // 2
            
            if mid == 0 and nums[mid] > nums[1]:
                return mid
            
            elif mid == len(nums) - 1 and nums[mid] > nums[mid - 1]:
                return mid
            

            elif nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
        
            
            elif mid == 0:
                low = mid + 1
            

            elif mid == len(nums) - 1:
                high = mid - 1

            elif nums[mid] > nums[mid - 1] and nums[mid] < nums[mid + 1]:
                low = mid + 1
            
            else:
                high = mid - 1
