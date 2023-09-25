test_cases = int(input())

def getMaxTeams(p, m, max_range):
    
    best = 0
    low, high = 0, max_range
    
    while low <= high:
        mid = low + (high - low) // 2
        
        if mid * 4 <= p + m:
            best = mid
            low = mid + 1
        else:
            high = mid - 1
    
    return best

for _ in range(test_cases):
    
    a, b = list(map(int, input().split()))
    max_teams = getMaxTeams(a, b, min(a, b))
    print(max_teams)
