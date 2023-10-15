class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s = s.split()
        nums = []
        
        for i in s:
            if i.isnumeric():
                nums.append(int(i))
        
        for i in range(len(nums) - 1):
            if nums[i] >= nums[i + 1]:
                return False
        
        return True