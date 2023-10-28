class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_dict = {}
        
        for i in range(len(nums)):
            if target - nums[i] in idx_dict:
                num_idx = idx_dict[target - nums[i]]
                return [num_idx, i]
            
            idx_dict[nums[i]] = i