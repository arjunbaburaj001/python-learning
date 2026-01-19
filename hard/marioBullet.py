# cook your dish here
t = int(input())

for _ in range(t):
    x, y, z = map(int, input().split())
    yx = y/x
    if z >= yx:
        print(int(z - yx))
    else:
        print(0)