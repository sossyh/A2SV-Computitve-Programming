class Solution:
    def power(self, num, val):
        if num == 1:
            return val

        if num % 2 == 0:
            return self.power(num // 2, val + 1)
        else:
            return self.power(num * 3 + 1, val + 1)
        
        
    def getKth(self, lo: int, hi: int, k: int) -> int:
        result = defaultdict(list)
        memo = {}

        for i in range(lo, hi + 1):
            power = None

            if i in memo:
                power = memo[i]
            else:
                power = self.power(i, 0)
            
            result[power].append(i)

     
        for i in result:
            if len(result[i]) >= 2:
                result[i].sort()
            
        powers = sorted(result)

        ans = []

        for i in powers:
            for j in result[i]:
                ans.append(j)

        return ans[k - 1]


        

        

