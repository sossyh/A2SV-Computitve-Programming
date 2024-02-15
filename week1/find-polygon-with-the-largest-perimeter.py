class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        total = sum(nums)

        for i in range(len(nums)):
            curr = nums[i]
            if total - curr > curr:
                return total
            
            total -= curr
        
        return -1

        
