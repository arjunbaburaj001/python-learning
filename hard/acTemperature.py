# cook your dish here
t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    
    if b >= max(a, c) :
        print("YES")
    else:
        print("NO")