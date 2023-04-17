class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        result=[]
        for i in range(len(words[0])):
            count=0
            for j in range(1,len(words)):
                word=[i for i in words[j]]
                if words[0][i] in word:
                    count+=1
                    word.remove(words[0][i])
                    words[j]="".join(word)
                        
            if count==(len(words)-1):
                result.append(words[0][i])
        return result