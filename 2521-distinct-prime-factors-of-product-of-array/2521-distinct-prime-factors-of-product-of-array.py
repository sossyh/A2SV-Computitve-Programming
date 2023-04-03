class Solution:
    def primefactorcalc(self, n):
        primefactors = set()
        i = 2
        while i*i <= n:
            while n % i == 0:
                primefactors.add(i)
                n //= i
            i += 1
        if n > 1:
            primefactors.add(n)
        return primefactors
            
            
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        ans = set()
        for i in nums:
            solution = self.primefactorcalc(i)
            ans = ans.union(solution)
        
        return len(ans)
        