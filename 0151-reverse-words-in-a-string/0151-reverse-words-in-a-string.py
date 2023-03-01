class Solution:
    def reverseWords(self, s: str) -> str:
        wordlst = s.split(" ")
        newwordlst = []
        for i in wordlst:
            if i != '':
                newwordlst.append(i)
                
        j,k = 0,len(newwordlst)-1
        while j < k:
            newwordlst[j],newwordlst[k] = newwordlst[k],newwordlst[j]
            j += 1
            k -= 1
        
        return " ".join(newwordlst)

