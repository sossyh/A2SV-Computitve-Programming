class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        d = defaultdict(list)
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                d[i+j].append(mat[i][j])
        
        
        ans = []
        
        for key in d:
            if key % 2 == 0:
                ans.extend(d[key][::-1])
            
            else:
                a = d[key]
                ans.extend(a)
        
        return ans