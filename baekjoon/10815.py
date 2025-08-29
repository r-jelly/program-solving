import sys

N = int(sys.stdin.readline())
nums_n = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
nums_m = list(map(int, sys.stdin.readline().split()))

deck = set()
for num in nums_n:
    deck.add(num)

answer = [1 if num in deck else 0 for num in nums_m]
print(*answer)