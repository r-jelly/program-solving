'''
Level: S4
Time: 07m43s
'''
import sys
from collections import defaultdict
input = lambda: sys.stdin.readline().strip()

def solution(N, ban_dict):
    answer = 0
    for n1 in range(1, N+1):
        for n2 in range(n1+1, N+1):
            for n3 in range(n2+1, N+1):
                if n2 in ban_dict[n1]:
                    continue
                if n3 in ban_dict[n2]:
                    continue
                if n1 in ban_dict[n3]:
                    continue
                answer += 1
    return answer

if __name__ == "__main__":
    N, M = list(map(int, input().split()))
    ban_dict = defaultdict(list)

    for _ in range(M):
        n1, n2 = list(map(int, input().split()))
        ban_dict[n1].append(n2)
        ban_dict[n2].append(n1)

    print(solution(N, ban_dict))
    