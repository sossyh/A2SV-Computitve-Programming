#User function Template for python3

class Solution:
    #Function to arrange all letters of a string in lexicographical 
    #order using Counting Sort.
    def countSort(self,arr):
        # code here
        count = [0 for i in range(26)]
        
        offset = ord("a")
        for i in arr:
            count[ord(i) - offset] += 1
        
        ans = ""
        for i in range(26):
            for _ in range(count[i]):
                ans += chr(ord("a")+i)
                
            
        
        return ans
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        arr = str(input())
        ob = Solution()
        print(ob.countSort(arr))

# } Driver Code Ends