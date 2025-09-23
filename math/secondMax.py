# cook your dish here
N = int(input())

for _ in range(N):
    nums = list(map(int, input().split()))
    nums.sort()
    print(nums[1])
    