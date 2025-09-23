t = int(input())

while t > 0:
    a, b, c = map(int, input().split())
    print('pass' if a+b >= 70 and a+c >= 70 and b+c >= 70 else 'fail')
    t -= 1
