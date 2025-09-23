def solve():
    d, n = map(int, input().split())
    ans = n
    for i in range(d):
        ans = ans * (ans + 1) // 2
    print(ans)

test = int(input())
for _ in range(test):
    solve()
