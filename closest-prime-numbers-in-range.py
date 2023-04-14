class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        ans = [-1, -1]
        arr = [True for i in range(right+1)]
        arr[0], arr[1] = False, False
        n = right
        mind = float("inf")

        i = 2
        while i * i <= n:
            if arr[i]:
                j = i * i
                while j <= n:
                    arr[j] = False
                    j += i
                
            i += 1
        
        primes = []
        for j in range(len(arr)-1, max(left, 2)-1, -1):
            if arr[j]:
                primes.append(j)

        for k in range(1,len(primes)):
            if primes[k-1] - primes[k] <= mind:
                ans = [primes[k], primes[k-1]]
                mind = primes[k-1] - primes[k]

        return ans