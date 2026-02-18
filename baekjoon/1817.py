'''
Level: S5
Time: 17m55s
'''
import sys
input = lambda: sys.stdin.readline().strip()

def solution(N, M):
    if N==0:
        return 0
    
    weights = list(map(int, input().split()))
    count = 1
    cur_weights = 0
    for weight in weights:
        if cur_weights + weight > M:
            cur_weights = 0
            count += 1
        cur_weights += weight

    return count


if __name__ == "__main__":
    N, M = list(map(int, input().split()))
    print(solution(N, M))