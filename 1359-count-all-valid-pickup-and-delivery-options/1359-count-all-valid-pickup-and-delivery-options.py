class Solution:
    def countOrders(self, n: int) -> int:
        #since we have 2 * n slots
        x = 2 * n
        
        #but for each of two slots half of them make the delivery before pickup so it should be reduced n times
        # x(x-1) / 2 * (x-2)(x-3) / 2 ........
        valid_ways = (factorial(2*n) // (2 ** n) ) % (10 ** 9 + 7)
        
        return valid_ways 