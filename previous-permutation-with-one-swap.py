class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:

        for i in range(len(arr)-1, -1, -1):
            if i-1 >= 0 and arr[i] < arr[i-1]:
                
                t = i
                j = i + 1

                while j < len(arr) and arr[j] < arr[i-1]:
                    if arr[j] != arr[j - 1]:
                        t = j
                    j += 1
                arr[i-1], arr[t] = arr[t], arr[i-1]
                return arr

        return arr