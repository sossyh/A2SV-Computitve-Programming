class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter_s1 = {}
        
        for char in s1:
            if char not in counter_s1:
                counter_s1[char] = 0
            counter_s1[char] += 1
        
        counter_s2 = {}
        
        start = 0
        
        for end in range(len(s2)):
            char = s2[end]
            
            if char not in counter_s2:
                counter_s2[char] = 0
            counter_s2[char] += 1
            
            if end >= len(s1):
                counter_s2[s2[start]] -= 1
                if counter_s2[s2[start]] == 0:
                    del counter_s2[s2[start]]
                
                start += 1
            
            if counter_s1 == counter_s2:
                return True
        
        
        return False