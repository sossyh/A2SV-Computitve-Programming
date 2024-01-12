class Solution:
    def count_vowel(self, s):
        vawels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        count = 0

        for char in s:
            if char in vawels:
                count += 1
        
        return count 

    def halvesAreAlike(self, s: str) -> bool:
        half = len(s) // 2

        first = self.count_vowel(s[:half])
        second = self.count_vowel(s[half:])

        return first == second
        