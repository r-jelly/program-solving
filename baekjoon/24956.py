'''
Level: G4
Time: 57m59s
'''
import sys
input = lambda: sys.stdin.readline().strip()

def solution(N: int, S: str) -> int:
    if N <= 3:
        return 0
    
    prev = [0, 0, 0, 0]
    for i in range(0, N):
        cur = prev.copy()
        if S[i] == 'W':
            cur[0] += 1
        elif S[i] == 'H':
            cur[1] += prev[0]
        elif S[i] == 'E':
            cur[2] += prev[1]
            cur[3] = prev[3]*2 + prev[2]
        prev = cur

    return cur[3] % (10**9+7)

if __name__ == "__main__":
    N = int(input())
    S = input()
    print(solution(N, S))