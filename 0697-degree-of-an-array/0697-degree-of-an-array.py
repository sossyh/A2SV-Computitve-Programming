class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq = Counter(nums)
        degree = 0
        d = {}
        
        for i in range(len(nums)):
            degree = max(freq[nums[i]], degree)
            if nums[i] not in d:
                d[nums[i]] = [i, i]
            else:
                d[nums[i]][1] = i
        
        min_len = inf
        
        for i in d:
            if freq[i] == degree:
                min_len = min(min_len, d[i][1] - d[i][0] + 1)
        
        return min_len
            