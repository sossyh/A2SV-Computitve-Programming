class Solution:
    def largestGoodInteger(self, num: str) -> str:
        result = ""
        l = 0
        sames = num[0]

        for r in range(1, len(num)):
            if num[l] == num[r]:
                sames += num[r]
            
            else:
                l = r
                sames = num[l]       

            if len(sames) > 3:
                sames = sames[:3]

            if len(sames) == 3 and (not result or int(sames) > int(result)):
                result = sames
        
        return result

