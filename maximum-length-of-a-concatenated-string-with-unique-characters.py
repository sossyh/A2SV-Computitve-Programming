class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def isunique(string):
            charsoccurence = [False for i in range(26)]

            for char in string:
                idx = ord(char) - ord('a')
                if charsoccurence[idx] == True:
                    return False
                
                charsoccurence[idx] = True

            return True

        ans = 0
        def backtracking(idx, lst):
            nonlocal ans
            if idx >= len(arr):
                string = "".join(lst)
                if isunique(string):
                    ans = max(ans, len(string))
                return
            
            lst.append(arr[idx])
            backtracking(idx + 1, lst)
            lst.pop()
            backtracking(idx + 1, lst)
        
        backtracking(0, [])

        return ans