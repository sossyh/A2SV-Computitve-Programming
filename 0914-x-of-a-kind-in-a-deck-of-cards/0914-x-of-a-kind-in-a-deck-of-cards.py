class Solution:
    def gcd(self, a,b):
        if b == 0:
            return a
        return self.gcd(b, a%b)
    
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = Counter(deck)
        gcdf = count[deck[0]]
        
        for i in count:
            gcdf = self.gcd(count[i],gcdf)
        
        if gcdf == 1:
            return False
        else:
            return True