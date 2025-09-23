# cook your dish here
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    
    if n >= k * (k + 1)/2:
        print("YES")
    else:
        print("NO")