class DisjointSet():
    def __init__(self, n):
        self.roots = {}
        self.rank = {}

        for i in n:
            self.roots[i] = i
            self.rank[i] = 0
    
    def find(self, x):
        if self.roots[x] != x:
            self.roots[x] = self.find(self.roots[x])
        
        return self.roots[x]
    
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)

        rankx = self.rank[rootx]
        ranky = self.rank[rooty]

        if rootx != rooty:
            if rankx == ranky:
                self.rank[rooty] += 1
            
            if rankx > ranky:
                self.roots[rooty] = rootx

            else:
                self.roots[rootx] = rooty
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        n = len(equations)
        chars = set()

        for i in equations:
            chars.add(i[0])
            chars.add(i[3])
        
        obj = DisjointSet(chars)

        for i, j, k, l in equations:
            if (j == '='):
                obj.union(i, l)
        
        for i, j, k, l in equations:
            if obj.connected(i, l):
                if j == '!':
                    return False

        return True