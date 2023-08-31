class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = Counter(s1.split())
        s2 = Counter(s2.split())
        ans = []
        
        for i in s1:
            if i not in s2 and s1[i] == 1:
                ans.append(i)
        
        for i in s2:
            if i not in s1 and s2[i] == 1:
                ans.append(i)
        
        
        return ans