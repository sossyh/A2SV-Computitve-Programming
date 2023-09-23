class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        d = {}
        start = 0
        currstr = ""
        result = []
        
        for end in range(len(s)):
            currstr += s[end]
            
            if end >= 9:
                if currstr not in d:
                    d[currstr] = 0
                d[currstr] += 1
                currstr = currstr[1:]
                start += 1
        
        for i in d:
            if d[i] >= 2:
                result.append(i)
        
        return result