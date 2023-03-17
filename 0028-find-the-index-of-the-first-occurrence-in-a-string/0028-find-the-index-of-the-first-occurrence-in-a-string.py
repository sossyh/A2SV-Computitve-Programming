class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        start = 0
        curr = ""
        n = len(needle)
        for end in range(len(haystack)):
            if haystack[end: end + n] == needle:
                return end
        return -1
