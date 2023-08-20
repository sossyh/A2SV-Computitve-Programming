class Solution:
    def finalString(self, s: str) -> str:
        rFaultyKeyboard = ""
        
        for i in s:
            if i == 'i':
                rFaultyKeyboard = rFaultyKeyboard[::-1]
            else:
                rFaultyKeyboard += i
        
        return rFaultyKeyboard
                