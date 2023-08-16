class Solution:
    def ispalindrom(self, string):
        i, j =0 , len(string) - 1
        
        while i < j:
            if string[i] != string[j]:
                return False
            i += 1
            j -= 1
        
        return True
            
    def partition(self, s: str) -> List[List[str]]:
        result = []
        
        def backtrack(num, lst):
            if num == "":
                result.append(lst[:])
                return 
            
            for i in range(len(num)):
                prefix = num[:i+1]
                
                if self.ispalindrom(prefix):
                    lst.append(prefix)
                    backtrack(num[i+1:], lst)
                    lst.pop()
        
        backtrack(s, [])
        
        return result
        