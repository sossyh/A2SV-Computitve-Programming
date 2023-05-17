class Disjoint:

    def __init__(self, size):
        self.rep = [ i for i in range(size)]
        self.rank = [ 1 for i in range(size)]
    
    def find(self, x):

        if self.rep[x] == x:
            return x
        
        the_rep = self.find(self.rep[x])
        self.rep[x] = the_rep

        return the_rep

    def union(self, x, y):
        repx = self.find(x)
        repy = self.find(y)

        rankx = self.rank[x]
        ranky = self.rank[y]

        if rankx < ranky:
            self.rep[repx] = repy
            self.rank[repy] = max(self.rank[repy], 1 + self.rank[repx])
        
        else:
            self.rep[repy] = repx
            self.rank[repx] = max(self.rank[repx], 1 + self.rank[repy])
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        unionfind = Disjoint(len(edges)+1)

        for i, j in edges:
            
            if unionfind.find(i) == unionfind.find(j):
                return [i, j]
                
            unionfind.union(i, j)