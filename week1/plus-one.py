class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string=""
        ans=[]
        for i in digits:
            string+=str(i)
        result=int(string)+1
        print(str(result))
        for i in str(result):
            ans.append(i)
        return ans