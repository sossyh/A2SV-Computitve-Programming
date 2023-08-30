class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans = ""
        carry = 0
        less = num1 if len(num1) < len(num2) else num2
        high = num1 if len(num1) >= len(num2) else num2
        
        offset = max(len(num1), len(num2)) - min(len(num1), len(num2))
        
        for i in range(max(len(num1), len(num2))-1, -1, -1):
            lesselement = 0
            if (i - offset) >= 0:
                lesselement = int(less[i-offset])
            
            
            currsum = lesselement + int(high[i]) + carry
            
            ans += str(currsum % 10)
            carry = currsum // 10
            
        
        if carry:
            ans += str(carry)
        
        return ans[::-1]
        
        
        
        
        
            