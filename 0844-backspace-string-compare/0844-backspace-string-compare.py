class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stacks = []
        stackt = []
        
        for i in s:
            if stacks and i == '#':
                stacks.pop()
            elif not stacks and i == "#":
                continue
            else:
                stacks.append(i)
        
        for i in t:
            if stackt and i == '#':
                stackt.pop()
            elif not stackt and i == "#":
                continue
            else:
                stackt.append(i)
        
        print(stacks, stackt)
        
        return stacks == stackt