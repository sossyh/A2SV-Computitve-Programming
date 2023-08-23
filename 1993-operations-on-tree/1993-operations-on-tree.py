class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.status = ["u" for i in range(len(parent))]
        self.tree = defaultdict(list)
        
        for i in range(len(parent)):
            self.tree[parent[i]].append(i)
        print(self.tree)

    def lock(self, num: int, user: int) -> bool:
        if self.status[num] == "u":
            self.status[num] = user
            return True
        else:
            return False
        

    def unlock(self, num: int, user: int) -> bool:
        if self.status[num] == user:
            self.status[num] = "u"
            return True
        else:
            return False
        

    def upgrade(self, num: int, user: int) -> bool:
        # print(num)
        i = num
        ancestorsLocked = False
       
        while i != 0:
            parent = self.parent[i]
            if self.status[parent] != "u":
                p = parent
            
                ancestorsLocked = True
                break

            i = parent

        tounlock = []
        queue = deque()
        queue.append(num)
        visited = set()
        visited.add(num)

        while queue:
            node = queue.popleft()

            for i in self.tree[node]:
                if i not in visited:
                    if self.status[i] != "u":
                        tounlock.append(i)
                    visited.add(i)
                    queue.append(i)
        
       

        if self.status[num] == "u" and tounlock != [] and not ancestorsLocked:

            for i in tounlock:
                self.status[i] = "u"

            self.status[num] = user

            return True

        return False







# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)