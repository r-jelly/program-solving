'''
Level: S4
Time: 02m21s
'''
import sys
input = lambda: sys.stdin.readline().strip()

if __name__ == "__main__":
    N_A, N_B = list(map(int, input().split()))
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))

    print(len(A-B) + len(B-A))
