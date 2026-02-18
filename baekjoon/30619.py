'''
Level: S2
Time: 24m26s
'''
import sys
input = lambda: sys.stdin.readline().strip()


def solution(A_dict, L, R):
    A = [-1] * len(A_dict)
    items = sorted(A_dict.items())
    for i, (person, idx) in enumerate(sorted(items[L-1:R], key=lambda x: x[1])):
        A_dict[L+i] = idx
    for person, idx in A_dict.items():
        A[idx] = person
    return A


if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    A_dict = {A[i]: i for i in range(len(A))}
    
    M = int(input())
    for _ in range(M):
        L, R = list(map(int, input().split()))
        print(*solution(A_dict.copy(), L, R))