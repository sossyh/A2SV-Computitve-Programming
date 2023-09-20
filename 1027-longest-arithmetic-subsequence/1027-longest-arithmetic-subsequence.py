class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        
        memo = defaultdict(dict)
        
        maxlen = 2
        
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                
                if diff in memo[j]:
                    memo[i][diff] = memo[j][diff] + 1
                else:
                    memo[i][diff] = 2
            
                maxlen = max(maxlen, memo[i][diff])
        
        return maxlen