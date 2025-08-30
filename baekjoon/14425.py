import sys
N, M = list(map(int, sys.stdin.readline().split()))

str_set = set()
for _ in range(N):
    string = sys.stdin.readline().strip()
    str_set.add(string)

count = 0
for _ in range(M):
    string = sys.stdin.readline().strip()
    count += 1 if string in str_set else 0
print(count)