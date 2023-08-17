from collections import defaultdict
from collections import deque

def checker(graph):
        queue = deque()
        queue.append(0)
        colors = [2] * n
        colors[0] = 0

        while queue:
            item = queue.popleft()
            for i in graph[item]:
                if colors[i] == colors[item]:
                        return False
                
                if colors[i] == 2:
                    queue.append(i)
                    colors[i] = not colors[item]
                    
        return True
        
while True:
    n = int(input())
    if n == 0:
        break

    l = int(input())
    graph = defaultdict(list)
    for i in range(l):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)

        
    if checker(graph):
        print("BICOLOURABLE.")
    else:
        print("NOT BICOLOURABLE.")
