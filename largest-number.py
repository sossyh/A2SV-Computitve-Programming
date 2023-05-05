class Solution:
    def comparator(self, n1, n2):
        if n2 + n1 > n1 + n2:
            return 1
        else:
            return 0
        
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if self.comparator(nums[i], nums[j]):
                    nums[i], nums[j] = nums[j], nums[i]

        ans = "".join(nums)

        return "0" if int(ans) == 0 else ans