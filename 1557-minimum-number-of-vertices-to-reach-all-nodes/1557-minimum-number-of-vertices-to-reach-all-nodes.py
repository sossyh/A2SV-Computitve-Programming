class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        result = set()
        destinaions = {}
        
        for i in range(len(edges)):
            item = edges[i]
            if item[1] not in destinaions:
                destinaions[item[1]] = 0
            destinaions[item[1]] += 1
        
        for j in range(len(edges)):
            item = edges[j]
            if item[0] not in destinaions:
                result.add(item[0])
        
        return result