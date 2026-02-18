'''
Level: G5
Time: 27m47s
'''
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    items = [list(map(int, input().split())) for _ in range(N)]

    energy = 0
    a_sum, b_sum = 0, 0
    for a, b in items:
        energy += a_sum * b + b_sum * a
        a_sum += a
        b_sum += b

    print(energy)

# 어떠한 숫자대로 합쳐도 값이 동일!