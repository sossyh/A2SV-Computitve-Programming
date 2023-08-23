class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        notequalpos = 0
        charnotequals1 = set()
        charnotequals2 = set()
        
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                notequalpos += 1
                charnotequals1.add(s1[i])
                charnotequals2.add(s2[i])
                
        
        return True if (notequalpos == 0   or notequalpos == 2) and charnotequals1 == charnotequals2 else False
        
        