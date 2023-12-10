class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        # do the structure in a graph(tree) form
        # will have the information (info_time) for each node
        # if a person who has no subordinates - it is the last person to know the info
        # maximizing the totla time of each person with no subordinate

        tree = defaultdict(list)

        min_time = -inf

        for i in range(n):
            boss = manager[i]
            tree[boss].append(i)
        
        queue = deque()
        visited = set()

        queue.append((headID, informTime[headID]))
        visited.add(headID)

        while queue:
            node, time = queue.popleft()

            min_time = max(min_time, time)

            for child in tree[node]:
                if child not in visited:
                    queue.append((child, time + informTime[child]))
                    visited.add(child)
        
        return min_time


        """
        time - O(n) + O(n) - o(2n) - O(n)

        space - O(n) + O(n) + O(n) - O(3n) - O(n)
        
        """

