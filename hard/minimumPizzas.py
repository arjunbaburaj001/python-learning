# cook your dish here
t = int(input())
x = 1
for _ in range(t):
    n, x = map(int, input().split())
    
    if (n*x)/4 == type(x):
        print(n*x)/4
    else:
        print(int((n*x+3) // 4))