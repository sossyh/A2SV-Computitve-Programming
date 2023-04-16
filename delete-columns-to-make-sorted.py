class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        newstrs = []

        for i in range(len(strs)):
            strs[i]=list(strs[i])
   
        for j in range(len(strs[0])):
   
            lst=[]
            for k in range(len(strs)):
                lst.append(strs[k][j])
            newstrs.append(lst)
   
        count=0
   
        for m in newstrs:
            slow=0
            fast=1
   
            while slow<len(m)-1:
                if ord(m[slow])>ord(m[fast]):
                    count+=1
                    break
                slow+=1
                fast+=1
   
        return count