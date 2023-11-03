class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = Counter(nums)
        count = 0
        
        for i in freq:
            count += (freq[i] * (freq[i] - 1)) // 2
        
        return count
