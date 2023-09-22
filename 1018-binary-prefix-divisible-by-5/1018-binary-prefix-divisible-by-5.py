class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        num = ""
        result = []
        
        for i in nums:
            num += str(i)
            intnum = int(num, 2)
            if intnum % 5 == 0:
                result.append(True)
            else:
                result.append(False)
        
        return result