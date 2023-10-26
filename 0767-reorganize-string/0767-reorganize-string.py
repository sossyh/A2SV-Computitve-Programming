class Solution:           
    def reorganizeString(self, s: str) -> str:
        freq = {}
        
        for i in s:
            if i not in freq:
                freq[i] = 0
            freq[i] += 1
        
        freq = dict(sorted(freq.items(), key = lambda item : item[1], reverse = True))
        max_freq = max(freq.values())
        slot = []
        
        count = 0
        for i in range(max_freq):
            count += 1
            for char in freq:
                if count <= freq[char]:
                    slot.append(char)
            
            
        see_another_option = False
        for i in range(len(slot) - 1):
            if slot[i] == slot[i + 1] or slot[i] == 0 or slot[i + 1] == 0:
                see_another_option = True
        
        if see_another_option:
            slot = [0] * len(s)


            for char in freq:
                i = 0
                charfreq = freq[char]
                while i < len(s) and charfreq != 0:
                    if slot[i] != 0:
                        i += 1
                    else:
                        slot[i] = char
                        i += 2
                        charfreq -= 1
                
            for i in range(len(slot) - 1):
                if slot[i] == slot[i + 1] or slot[i] == 0 or slot[i + 1] == 0:
                    return ""
                        
        
        return "".join(slot)
            