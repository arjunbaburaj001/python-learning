# cook your dish here
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    count = n + max(0, n - m)
    
    print(count)