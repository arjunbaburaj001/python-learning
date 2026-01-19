# cook your dish here
t = int(input())

for _ in range(t):
    n, a, b = map(int, input().split())
    #n = number of episodes
    #a = even indexed episodes amount of minutes
    #b = odd indexed episode amount of minutes
    even_indexed = n // 2
    odd_indexed = (n + 1) // 2
    print(even_indexed * a + odd_indexed * b)