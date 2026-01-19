# cook your dish here
t = int(input())

for _ in range(t):
    b1, b2, b3 = map(int, input().split())
    
    if b1 + b2 + b3 <= 1:
        print("Water Filling Time")
    else:
        print("Not now")