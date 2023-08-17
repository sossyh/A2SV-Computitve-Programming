class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        lst = s.split(" ")
        
        return " ".join(lst[:k])