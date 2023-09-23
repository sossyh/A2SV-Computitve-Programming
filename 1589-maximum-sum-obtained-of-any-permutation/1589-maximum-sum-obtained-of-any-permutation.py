class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        queryarray = [0] * len(nums)
        
        for i, j in requests:
            queryarray[i] += 1
            
            if j + 1 < len(nums):
                queryarray[j+1] -= 1
        
        summ = queryarray[0]
        
        for i in range(1, len(nums)):
            summ += queryarray[i]
            queryarray[i] = summ
        
        queryarray.sort(reverse = True)
        nums.sort(reverse = True)
        
        ans = 0
        
        for i in range(len(nums)):
            ans += nums[i] * queryarray[i]
            ans = ans % (pow(10,9) + 7)
        
        return ans
            