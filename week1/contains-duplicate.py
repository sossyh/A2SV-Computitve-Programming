class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = {}
        for i in range(len(nums)):
            if nums[i] in hashset:
                    return True
            
            hashset[nums[i]] = i
        return False