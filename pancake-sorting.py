class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(i):
            arr[0:i] = reversed(arr[0:i])

        result = []
        n = len(arr)
        for i in range(len(arr)):
            idx = arr.index(max(arr[:n-i]))
            flip(idx + 1)
            result.append(idx + 1)
            flip(len(arr) - i)
            result.append(len(arr) - i)
        
        return result