class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq = Counter(nums)
        degree = 0
        
        for i in freq:
            degree = max(degree, freq[i])
        
        min_len = inf
        start = 0
        d = Counter()
        curr_degree = 0
        
        for end in range(len(nums)):
            elet = nums[end]
            d[elet] += 1
            curr_degree = max(curr_degree, d[elet])
            
            while curr_degree >= degree:
                if curr_degree == degree:
                    min_len = min(min_len, end - start + 1)
                
                left = nums[start]
                if d[left] == curr_degree:
                    curr_degree -= 1
                d[left] -= 1
                start += 1
        
        return min_len