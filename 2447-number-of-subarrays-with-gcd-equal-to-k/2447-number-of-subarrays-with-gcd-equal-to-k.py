class Solution:
    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a%b)
    
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        count = 0
        
        for i in range(len(nums)):
            currgcd = nums[i]
            for j in range(i, len(nums)):
                a =self.gcd(currgcd, nums[j]) 
                if a == k:
                    count += 1
                currgcd = a
                    
                
                
            
        return count
                
                
                
        
        
        