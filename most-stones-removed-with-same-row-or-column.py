class Disjointset():
    def __init__(self, lst):
        self.parent = {}
        self.size = {}

        for i in lst:
            self.parent[tuple(i)] = tuple(i)
        for i in lst:
            self.size[tuple(i)] = 1
        
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]
    
    def union(self, x, y):
        parx = self.find(x)
        pary = self.find(y)

        if parx == pary:
            return

        if self.size[parx] > self.size[pary]:
            self.parent[pary] = parx
            self.size[parx] += self.size[pary]
            self.size[pary] = 1
        else:
            self.parent[parx] = pary
            self.size[pary] += self.size[parx]
            self.size[parx] = 1


    
    def connected(self, x, y):
        return self.find(x) == self.find(y)
    
    def sizeofconnection(self):
        return self.size


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        obj = Disjointset(stones)

        for i in range(len(stones)):
            for j in range(i+1, len(stones)):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    obj.union(tuple(stones[i]), tuple(stones[j]))
        
        connections = obj.sizeofconnection()
        print(connections)
        result = 0
        for i in connections:
            result += connections[i] - 1
        
        return result