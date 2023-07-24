class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingname = kingName
        self.relation = defaultdict(list)
        self.dead = set()
        

    def birth(self, parentName: str, childName: str) -> None:
        self.relation[parentName].append(childName)
        

    def death(self, name: str) -> None:
        self.dead.add(name)
#         queue = deque()
#         visited = set()
#         queue.append(self.kingname)
        
#         while queue:
#             item = queue.popleft()
#             for i in range(len(self.relation[item])):
                
#                 if self.relation[item][i] == name:
#                     self.dead.add(name)
                    
#                 if self.relation[item][i] not in visited:
#                     queue.append(self.relation[item][i])
#                     visited.add(self.relation[item][i])
        
        
    def getInheritanceOrder(self) -> List[str]:
        order = []
        
        def preorder(name):
            if not name:
                return
            
            if name not in self.dead:
                order.append(name)
            for i in self.relation[name]:
                preorder(i)
        
        preorder(self.kingname)
        
        return order
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()