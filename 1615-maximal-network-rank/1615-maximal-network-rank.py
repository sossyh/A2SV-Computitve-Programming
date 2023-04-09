class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        maxRank = 0
        verticeRank = collections.defaultdict(set)
        
        for i in range(len(roads)):
            item = roads[i]
            verticeRank[item[0]].add(item[1])
            verticeRank[item[1]].add(item[0])
        
        for j in range(n):
            for k in range(j+1,n):
                connection = 1 if j in verticeRank[k] else 0
                maxRank = max(maxRank, len(verticeRank[j]) + len(verticeRank[k]) - connection )
        
        return maxRank
        