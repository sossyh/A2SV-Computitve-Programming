class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        result = [1 for _ in range(n)]
        visited = set()

        tree = defaultdict(list)
        for i, j in edges:
            tree[i].append(j)
            tree[j].append(i)
        
        def dfs(vertex):
            if len(tree[vertex]) == 1 and tree[vertex][0] in visited:
                chars = [0 for i in range(26)]
                chars[ord(labels[vertex]) - 97] = 1
                return chars
                
            visited.add(vertex)
            chars = [0 for i in range(26)]
            

            for i in tree[vertex]:
                if i not in visited:
                    a = dfs(i)
                    for j in range(len(a)):
                        if a[j]:
                            chars[j] += a[j]
            
            
            vertexlable = labels[vertex]
            
            result[vertex] += chars[ord(vertexlable) - 97]
            chars[ord(labels[vertex]) - 97] += 1
            
            return chars
                        
            
        a = dfs(0)
        
        
        return result
            


        

