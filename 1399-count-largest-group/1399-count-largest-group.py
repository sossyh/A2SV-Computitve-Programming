class Solution:
    def countLargestGroup(self, n: int) -> int:
        eachcount = defaultdict(int)
        
        for i in range(1, n+1):
            num = [int(k) for k in str(i)]
            eachcount[sum(num)] += 1
        
        mc = max(eachcount.values())
        
        ans = 0
        for i in eachcount:
            if eachcount[i] == mc:
                ans += 1
            
        return ans
        