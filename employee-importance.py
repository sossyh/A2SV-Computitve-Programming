"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        d = {e.id : e for i, e in enumerate(employees)} 
        importancecount = 0
        visited = set()

        def dfs(emp):
            nonlocal importancecount
            if emp.id in visited:
                return
            visited.add(emp.id)
            importancecount += emp.importance
            for subs in emp.subordinates:
                dfs(d[subs])
        
        
        dfs(d[id])

        return importancecount