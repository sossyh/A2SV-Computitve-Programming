class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        result = []
        newmat = []

        for m in (mat):
            newmat += m

        if r*c < len(newmat):
            return mat
        
        l = 0
        for i in range(r):
            row = []

            for j in range(c):
                if l > len(newmat)-1:
                    return mat
                row.append(newmat[l])
                l += 1
            result.append(row)
            
        return result