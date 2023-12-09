class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # accessing two elements form i-th row and j-th col
        # swap the values [i][j] and [j][i]
        # return the matrix
        # a set which tracks the exchagend cells

        """
        i, j = 1, 0
        martix[0][1], matrix[1][0] = martix[1][0], matrix[0][1]

        [[1,2,3]            
         [4,5,6]
         [7,8,9]]

        ans = [[1,4,7] 
               [2,5,6]
               [3,8,9]]

        n = len(matrix)
        n == len(matrix)(row) == len(matrix[0])(column)

        time == n * n = n^2
        assymptotic time == n**2
        space = O(n ** 2 - n) 
        assymptotic space --> O(n**2)

        """

        result = [[0] * len(matrix) for i in range(len(matrix[0]))] 

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                result[j][i] = matrix[i][j]


        return result




         