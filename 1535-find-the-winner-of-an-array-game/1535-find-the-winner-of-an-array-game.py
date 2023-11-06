class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr):
            return max(arr)
        
        wins = {}
        while True:
            if arr[0] > arr[1]:
                if arr[0] not in wins:
                    wins[arr[0]] = 0
                wins[arr[0]] += 1
                if wins[arr[0]] == k:
                    return arr[0]
                
                a = arr[1]
                del arr[1]
                arr.append(a)
                
            else:
                if arr[1] not in wins:
                    wins[arr[1]] = 0
                wins[arr[1]] += 1
                
                if wins[arr[1]] == k:
                    return arr[1]
                
                temp = arr[0]
                arr[0] = arr[1]
                del arr[1]
                arr.append(temp)
                
                
                
        