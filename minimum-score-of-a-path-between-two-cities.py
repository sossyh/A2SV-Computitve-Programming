class DisjointSet():
    def __init__(self, n):
        self.roots = [i for i in range(n)]
        self.rank = [0 for i in range(n)]
    
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
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        ob = DisjointSet(n+1)

        for from_, to, weight in roads:
            ob.union(from_, to)
        
        ans = float("inf")
        for from_, to, weight in roads:
            temp = ob.connected(n, from_)

            print(from_, to, temp)
            if temp:
                ans = min(ans, weight)
        
        return ans