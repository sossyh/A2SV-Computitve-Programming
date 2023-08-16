class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        sequence = []
        if len(num) <= 2:
            return False
        
        def backtrack(idx, num):
            if num == "":
                return True
            
            
            for i in range(len(num)):
                prefix = num[:i+1]
                if idx <= 1:
                    if prefix == '0' or prefix[0] != '0':
                        sequence.append(int(prefix))
                        if backtrack(idx+1, num[i+1:]) and len(sequence) >= 3:
                            return True
        
                        sequence.pop()
                else:
                    if prefix == '0' or prefix[0] != '0':
                        if int(prefix) == sequence[idx-1] + sequence[idx-2]:
                            sequence.append(int(prefix))
                            if backtrack(idx+1, num[i+1:]):
                                return True
                                
                            sequence.pop()
        
        
        
        return backtrack(0, num)    
            