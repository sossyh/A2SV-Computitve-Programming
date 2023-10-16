class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        res = [1]
        prev = self.getRow(rowIndex - 1)
        for i in range(1, rowIndex):
            res.append(prev[i-1] + prev[i])
        
        res.append(1)
        
        return res