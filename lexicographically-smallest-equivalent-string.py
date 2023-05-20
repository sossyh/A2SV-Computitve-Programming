class DisjointSet():
    def __init__(self, lst):
        self.parent = {}
        self.size = {}

        for i in lst:
            self.parent[(i)] = (i)
        
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]
    
    def union(self, x, y):
        parx = self.find(x)
        pary = self.find(y)

        if parx == pary:
            return

        if parx < pary:
            self.parent[pary] = parx
        else:
            self.parent[parx] = pary



class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        obj = DisjointSet(s1+s2)
        print(obj.parent)
        for i in range(len(s1)):
            obj.union(s1[i], s2[i])
        
        ans = ""
        for i in baseStr:
            if i not in s1 and i not in s2:
                ans += i
                continue
            ans += obj.find(i)
        
        return ans