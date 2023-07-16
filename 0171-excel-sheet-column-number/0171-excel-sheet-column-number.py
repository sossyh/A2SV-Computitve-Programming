class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        total = 0
        digit = 0
        
        for i in range(len(columnTitle)-1, -1, -1):
            if i == len(columnTitle)- 1:
                total += ((ord(columnTitle[i]) - 65) + 1)
            else:
                total += pow(26, digit)  * ((ord(columnTitle[i]) - 65) + 1)
            digit += 1
        
        return total