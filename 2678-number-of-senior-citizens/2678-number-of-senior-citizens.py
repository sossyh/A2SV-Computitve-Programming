class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        
        for i in range(len(details)):
            count += 1 if  int(details[i][11:13]) > 60 else 0
        
        return count