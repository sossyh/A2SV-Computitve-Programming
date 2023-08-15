class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []  
        
        
        def backtracking(idx, s, ans):
            
            if s == "" and idx == 4:
                result.append(ans[:-1])
            
            for i in range(len(s)):
                prefix = s[:i+1]
                
                if int(prefix) >= 0 and int(prefix) <= 255 and idx <= 4:
                    if prefix == '0' or prefix[0] != '0':
                        backtracking(idx+1, s[i+1:], ans + prefix + '.')
        
        backtracking(0, s, "")
        
        return result
                