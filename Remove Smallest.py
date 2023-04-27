t = int(input())
for i in range(t):
    length = int(input())
    arr = sorted(list(map(int, input().split())))
    
    while True:
        if len(arr) == 1 or arr[1] - arr[0] > 1:
            break
        
        if arr[1] - arr[0] <= 1:
            arr = arr[1:]
    
    if len(arr) == 1:
        print("YES")
    else:
        print("NO")
