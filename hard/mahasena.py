import sys
f = sys.stdin
n = int(f.readline())
cnt = 0
A = [int(x) for x in f.readline().split()]
for i in range(0, n):
	if A[i] % 2 == 0:
		cnt += 1
if cnt > n - cnt:
	print("READY FOR BATTLE")
else:
	print("NOT READY")