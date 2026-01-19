# cook your dish here
t = int(input())

for _ in range(t):
    a, b, c, d = map(int, input().split())
    print(max(a, b) + max(c, d))