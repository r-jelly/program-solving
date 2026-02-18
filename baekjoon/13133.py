'''
Level: S5
Time: 09m08s
'''
import sys
from collections import Counter
input = lambda: sys.stdin.readline().strip()

def solution(parents, remove_list):
    answer = 0
    for i, (p1, p2) in enumerate(parents):
        if p1==0 or p1 in remove_list:
            continue
        elif p2==0 or p2 in remove_list:
            continue
        elif i+1 in remove_list:
            continue
        else:
            answer += 1
    return answer


if __name__ == "__main__":
    N = int(input())
    parents = [list(map(int, input().split())) for _ in range(N)]
    M = int(input())
    remove_list = list(map(int, input().split()))

    print(solution(parents, remove_list))