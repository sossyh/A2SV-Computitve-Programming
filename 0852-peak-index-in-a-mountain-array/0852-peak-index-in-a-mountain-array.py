class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low, high = 0, len(arr) - 1
        best = 0
        
        while low <=high:
            mid = low + (high - low)//2
            
            if arr[mid] > arr[mid -1] and arr[mid] > arr[mid+1]:
                return mid
            
            if arr[mid-1] > arr[mid]:
                high = mid
                
            else:
                low = mid + 1
        
        
                
         