class DisjointSet():
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]
    
    def find(self, x):
        if self.parent[x] != x:
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
        
        else:
            self.parent[parx] = pary
            self.size[pary] += self.size[parx]


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:

        ans = list(s)
        indexgroup = defaultdict(list)
        chargroup = defaultdict(list)

        obj = DisjointSet(len(s))
        for i, j in pairs:
            obj.union(i, j)
        
        for i in range(len(s)):
            a = obj.find(i)
            indexgroup[a].append(i)
            chargroup[a].append(s[i])
        
        for i in indexgroup:
            idx = sorted(indexgroup[i])
            chars = sorted(chargroup[i])

            for j in range(len(idx)):
                ans[idx[j]] = chars[j]
        
        return "".join(ans)