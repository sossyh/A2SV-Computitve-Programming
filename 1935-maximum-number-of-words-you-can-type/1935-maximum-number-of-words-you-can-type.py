class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text = text.split()
        broken = set(brokenLetters)
        count = len(text)
        
        for word in text:
            for c in word:
                if c in broken:
                    count -= 1
                    break
        
        return count
                
        