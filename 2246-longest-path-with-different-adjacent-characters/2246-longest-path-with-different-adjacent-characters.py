class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        tree = defaultdict(list)
        ans = 1
        
        for i in range(1, len(parent)):
            tree[parent[i]].append(i)
        
        def dfs(root):
            nonlocal ans
            if tree[root] == []:
                return 1
            
            firstmax, secondmax = 0, 0
            
            for node in tree[root]:
                # if s[node] != s[root]:
                    value = dfs(node)
                    if s[node] != s[root]:
                        if value >= firstmax:
                            secondmax = firstmax
                            firstmax = value
                        elif value > secondmax and value < firstmax:
                            secondmax = value

            
            
            ans = max(ans, firstmax + secondmax + 1)
                
            return firstmax+1
        
        dfs(0)
        
        return ans
                