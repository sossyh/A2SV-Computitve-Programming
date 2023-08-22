class Solution:
    def minTimeToType(self, word: str) -> int:
        currpt = 'a'
        minSeconds = 0
        
        for i in word:
            clockwise = abs(ord(i) - ord(currpt))
            counterclockwise = 26 - clockwise
            
            minSeconds += min(clockwise, counterclockwise) + 1
            
            currpt = i
        
        return minSeconds
        