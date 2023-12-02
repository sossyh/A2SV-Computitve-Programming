class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # will map each digit 2 - 9
        # will track visited done via index
        # slice and pass it to the recursive function
        # will have a base case which adds to the global result function when the 

        result = []

        hashmap = { "2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl", "6" : "mno", "7" : "pqrs", "8" : "tuv", "9" : "wxyz"}

        def backtracking(idx, curr):
            if idx >= len(digits):
                result.append(curr)
                return
            

            chars = hashmap[digits[idx]]

            for c in chars:
                backtracking(idx + 1, curr + c)
        

        backtracking(0, "")

        return result if digits else []