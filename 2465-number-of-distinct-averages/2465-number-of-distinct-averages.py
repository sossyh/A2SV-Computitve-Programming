class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        num = set()
        i, j = 0, len(nums) - 1
        nums.sort()
        
        while i < j:
            ave = (nums[i]+nums[j]) / 2
            num.add(ave)
            i += 1
            j -= 1
        
        return len(num)