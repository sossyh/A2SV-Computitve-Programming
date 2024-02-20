class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sums = sum(nums)
        n = len(nums)

        total = n * (n + 1) / 2

        return int(total - sums)