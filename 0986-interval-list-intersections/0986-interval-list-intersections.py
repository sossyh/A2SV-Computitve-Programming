class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = []
        
        for i, j in firstList:
            for k, m in secondList:
                if (k <= j and k >= i) or (m >= i and m <= j) or (i >= k and i <= m) or (j >= k and j <= m):
                    inter = [max(i, k), min(m, j)]                    
                    result.append(inter)
        
        return result