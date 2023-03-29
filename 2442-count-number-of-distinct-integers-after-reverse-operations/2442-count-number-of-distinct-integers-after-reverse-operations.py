class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        result = nums[:]
        
        for i in range(n):
            reversednum = 0
            while nums[i] != 0:
                digit = nums[i] % 10
                reversednum = digit + reversednum * 10
                nums[i] //= 10
                
            result.append(reversednum)
        
        return len(set(result))
