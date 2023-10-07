class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        matrix = [[inf for i in range(numCourses)] for i in range(numCourses)]
        
        for i, j in prerequisites:
            matrix[i][j] = 1
        
        for i in range(numCourses):
            matrix[i][i]  = 0
        
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    matrix[i][j] = min(matrix[i][j], matrix[k][j] + matrix[i][k])
        
        result = []
        
        for i, j in queries:
            if matrix[i][j] != inf:
                result.append(True)
            else:
                result.append(False)
        
        return result