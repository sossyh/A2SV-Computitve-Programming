class Solution:
    def reformat(self, s: str) -> str:
        strings = []
        nums = []
        ans = ""
        
        for i in s:
            if i.isdigit():
                nums.append(i)
            else:
                strings.append(i)
        
        if abs(len(strings) - len(nums)) == 0 or abs(len(strings) - len(nums)) == 1:
            if len(strings) > len(nums):
                for i in range(len(nums)):
                    ans += strings[i]
                    ans += nums[i]
                ans += strings[-1]
            
            else:
                for i in range(len(strings)):
                    ans += nums[i]
                    ans += strings[i]
                
                if len(nums) > len(strings):
                    ans += nums[-1]
        
        return ans
            