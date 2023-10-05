class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        
        freq = Counter(nums)
        nums.sort()
        lonely_nums = []
        
        for i in range(len(nums)):
            if i == 0:
                if freq[nums[i]] == 1 and nums[i] + 1 != nums[i + 1]:
                    lonely_nums.append(nums[i])
            
            elif i == len(nums) - 1:
                if freq[nums[i]] == 1 and nums[i-1] + 1 != nums[i]:
                    lonely_nums.append(nums[i])
            
            else:
                if freq[nums[i]] == 1 and nums[i] + 1 != nums[i + 1] and nums[i-1] + 1 != nums[i]:
                    lonely_nums.append(nums[i])
        
        
        return lonely_nums
            
        