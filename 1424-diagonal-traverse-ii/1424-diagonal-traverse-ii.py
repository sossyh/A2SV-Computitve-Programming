class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        sum_row = []
        
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                val = (i+j, j, nums[i][j])
                sum_row.append(val)
        
        sum_row.sort()
        
        diagonal_traverse = []
        
        for _, _, val in sum_row:
            diagonal_traverse.append(val)
        
        return diagonal_traverse
        
        