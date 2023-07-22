class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        a = Counter(candyType)
        
        if len(a) == len(candyType) // 2:
            return len(a)
        
        elif len(a) > len(candyType) // 2:
            return len(candyType) // 2
        
        elif len(a) < len(candyType) // 2:
            return len(a)
        