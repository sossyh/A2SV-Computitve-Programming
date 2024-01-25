class Solution:
    def summation(self, n):
        ans = 0
        for i in range(n):
            ans += i
        
        return ans

    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = Counter(nums)
        ans = 0

        for key in freq:  
            ans += self.summation(freq[key]) 
        
        return ans