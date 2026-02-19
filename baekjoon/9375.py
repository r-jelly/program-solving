'''
Level: S3
Time: 10m00s
'''
import sys
from collections import defaultdict
input = lambda: sys.stdin.readline().strip()

def solution(cloth_dict: dict) -> int:
    if not cloth_dict:
        return 0
    
    answer = 1
    for type, names in cloth_dict.items():
        answer *= len(names) + 1
    return answer - 1


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        clothes = defaultdict(list)
        for _ in range(N):
            name, type = input().split()
            clothes[type].append(name)

        print(solution(clothes))
