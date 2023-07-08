class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        dist = [0] * k
        minUnfairness = inf
        

        def backtrack(idx):
            nonlocal minUnfairness
            if idx == len(cookies):
                minUnfairness = min(minUnfairness, max(dist))
                return
            
            if minUnfairness <= max(dist):
                return
            
            for i in range(k):
                dist[i] += cookies[idx]
                backtrack(idx+1)
                dist[i] -= cookies[idx]
            

        backtrack(0)
        
        return minUnfairness
                
                