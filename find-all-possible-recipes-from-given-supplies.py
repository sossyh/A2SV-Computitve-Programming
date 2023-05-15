class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        count = defaultdict(int)
        graph = defaultdict(list)
        result = set()
        s = set(supplies)
        queue = deque(supplies)

        for i in range(len(ingredients)):
            for j in ingredients[i]:
                graph[j].append(recipes[i])

        for i in range(len(recipes)):
            count[recipes[i]] = len(ingredients[i])
        
        recipes = set(recipes)
        while queue:

            item = queue.popleft()
            if item in recipes:
                result.add(item)
            
            for i in graph[item]:
                count[i] -= 1
                if count[i] == 0:
                    queue.append(i)
                
                    
            
        return result