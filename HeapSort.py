#User function Template for python3

class Solution:
    # Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        large = i
        left = i * 2 + 1
        right = i * 2 + 2
        if left < n and arr[large] < arr[left]:
            large = left
        if right < n and arr[large] < arr[right]:
            large = right
        if i != large:
            arr[i], arr[large] = arr[large], arr[i]
            self.heapify(arr, n, large)
    # Function to build a Heap from array.
    def buildHeap(self,arr,n):
        for i in range(n//2-1, -1, -1):
            self.heapify(arr, n, i)
            
    # Function to sort an array using Heap Sort.  
    def HeapSort(self, arr, n):
        self.buildHeap(arr, n)
        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0)
            
