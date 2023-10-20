class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        
        negative = False
        
        if num < 0:
            negative = True
            
        base7_num = ""
        
        num = abs(num)
        while num:
            remainder = num % 7
            # print(remainder)
            base7_num += str(remainder)
            num //= 7
        
        base7_num = base7_num[::-1]
        
        return base7_num if not negative else '-' + base7_num
            