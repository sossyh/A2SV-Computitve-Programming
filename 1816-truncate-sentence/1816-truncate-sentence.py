class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        lst = s.split(" ")
        lst = lst[:k]
        ans = ""
        
        for i in range(len(lst)):
            if i == len(lst) -1:
                ans += lst[i]
            else:
                ans += (lst[i] + " ")
            
        
        return ans