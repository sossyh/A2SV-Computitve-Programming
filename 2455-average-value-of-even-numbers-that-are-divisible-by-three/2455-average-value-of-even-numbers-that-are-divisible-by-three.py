class Solution:
    def averageValue(self, nums: List[int]) -> int:
        count, summ = 0, 0
        
        for i in nums:
            if i % 6 == 0:
                summ += i
                count += 1
        
        ans = summ / count if count != 0 else 0
        
        return int(ans)
        