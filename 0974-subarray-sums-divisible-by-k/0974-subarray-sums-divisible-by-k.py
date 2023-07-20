class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        Rcount = [0] * k
        summ = 0
        
        for i in nums:
            summ += i % k
            Rcount[summ%k] += 1
        
        res = Rcount[0]
        
        for i in range(len(Rcount)):
            res += (Rcount[i] * (Rcount[i] - 1)) // 2
        
        return res
        