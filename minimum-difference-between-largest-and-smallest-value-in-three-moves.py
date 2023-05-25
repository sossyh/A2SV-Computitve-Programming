class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0

        nums.sort()
        candidate = []

        candidate.append(nums[-4] - nums[0])
        candidate.append(nums[-1] - nums[3])
        candidate.append(nums[-2] - nums[2])
        candidate.append(nums[-3] - nums[1])

        return min(candidate)