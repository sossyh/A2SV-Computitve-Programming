def rangegcd(a, b):
    return a if a == b else 1

c, d = map(int, input().split())
ans = rangegcd(c, d)
print(ans)
