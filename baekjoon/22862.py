'''
Level: G5
Time:
'''
import sys
input = lambda: sys.stdin.readline().strip()

def solution(N, K, S):
    max_length = 0
    first = last = 0
    cur_jump = 0
    
    while first <= last and first < N:
        if cur_jump <= K and last < N:
            if S[last]%2==1:
                cur_jump += 1
            last += 1
        else:
            if S[first]%2==1:
                cur_jump -= 1
            first += 1

        max_length = max(
            max_length,
            last - first - cur_jump
        )
    return max_length

if __name__ == "__main__":
    N, K = list(map(int, input().split()))
    S = list(map(int, input().split()))
    print(solution(N, K, S))