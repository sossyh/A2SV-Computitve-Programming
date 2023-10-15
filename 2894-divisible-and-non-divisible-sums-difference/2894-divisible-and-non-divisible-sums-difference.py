class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        divisible, notdivisible = 0, 0
        
        for i in range(1, n + 1):
            if i % m == 0:
                divisible += i
            else:
                notdivisible += i
        
        return notdivisible - divisible