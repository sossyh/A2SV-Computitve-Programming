class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low, high = 0, len(arr) - 1
    
        while low <= high:
            mid = low + (high - low) // 2

            if mid > 0 and mid < len(arr) - 1 and arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return mid

            if mid == 0:
                low = mid + 1

            elif mid == len(arr) - 1:
                high = mid - 1

            elif arr[mid] > arr[mid - 1] and arr[mid] < arr[mid + 1]:
                low = mid + 1

            else:
                high = mid - 1