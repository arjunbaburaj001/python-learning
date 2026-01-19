# cook your dish here
t = int(input())

#x = schools
#y = students
#z = students that passed

for _ in range(t):
    x, y, z = map(int, input().split())
    
    if (x*y)/2 < z:
        print("YES")
    else:
        print("NO")
    