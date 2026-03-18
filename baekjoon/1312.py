'''
Level: S5
Time: 03m15s
'''
import sys
input = lambda: sys.stdin.readline().strip()


if __name__ == "__main__":
    A, B, N = list(map(int, input().split()))
    print(A*10**N // B % 10)