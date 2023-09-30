class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        news = ""
        ans = ""
        
        for i in s:
            if i != '-':
                news += i
        
        m = k
        inters = ""
        for i in range(len(news)-1,-1,-1):
            if m == 0:
                ans += inters + '-'
                m = k - 1
                inters = news[i].upper()
            else:
                inters += news[i].upper()
                m -= 1
        
        ans += inters
        
        return ans[::-1]
            
            
        