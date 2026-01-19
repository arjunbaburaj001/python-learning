# cook your dish here
t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    age = list(map(int, input().split()))
    count = 0
    
    for item in age:
        if item >= x:
            count +=1
        
    print(count)
    
        