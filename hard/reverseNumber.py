# cook your dish here
t = int(input())

for _ in range(t):
    n = int(input())
    
    string = str(n)
    reversedstring = string[::-1]
    reversednumber = int(reversedstring)
    print(reversednumber)
    