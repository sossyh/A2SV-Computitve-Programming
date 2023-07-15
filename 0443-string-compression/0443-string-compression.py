class Solution:
    def compress(self, chars: List[str]) -> int:
        l, r = 0, 1
        k = 0
        count = 1

        while r < len(chars):
            if chars[l] == chars[r]:
                r += 1
                count += 1
            else:
                chars[k] = chars[l]
                k += 1
                if count != 1:
                    newc = str(count)
                    for i in range(len(newc)):
                        chars[k] = newc[i]
                        k += 1
                
                count = 1
                l = r
                r += 1

        chars[k] = chars[l]
        k += 1
        if count != 1:
            newc = str(count)
            for i in range(len(newc)):
                chars[k] = newc[i]
                k += 1
        
        return k
