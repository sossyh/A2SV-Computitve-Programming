class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text = text.split()
        third = []
        
        for i in range(len(text)-1):
            if text[i] == first and text[i+1] == second and i+2 < len(text):
                third.append(text[i+2])
        
        
        return third
            