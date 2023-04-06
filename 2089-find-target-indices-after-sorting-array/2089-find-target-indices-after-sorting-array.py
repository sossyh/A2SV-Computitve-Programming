class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        ans = []
        for j in range(len(nums)):
            if nums[j] == target:
                ans.append(j)
        return ans
                

