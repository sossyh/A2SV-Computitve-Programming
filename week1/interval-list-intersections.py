class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        result = []

        while i < len(firstList) and j < len(secondList):
            if firstList[i][0] > secondList[j][1]:
                j += 1
            
            elif secondList[j][0] > firstList[i][1]:
                i += 1
            
            elif firstList[i][0] <= secondList[j][0] and secondList[j][1] <= firstList[i][1]:
                result.append([secondList[j][0], secondList[j][1]])
                j += 1
            
            elif secondList[j][0] <= firstList[i][0] and secondList[j][1] >= firstList[i][1]:
                result.append([firstList[i][0], firstList[i][1]])
                i += 1
            
            elif secondList[j][0] <= firstList[i][1] < secondList[j][1]:
                result.append([secondList[j][0], firstList[i][1]])
                i += 1

            elif firstList[i][0] <= secondList[j][1] < firstList[i][1]:
                result.append([firstList[i][0], secondList[j][1]])
                j += 1
        
        return result
            
