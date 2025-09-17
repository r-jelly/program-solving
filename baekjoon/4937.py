'''
Level: S2
Time: 28m08s
'''

import sys
input = sys.stdin.readline

def solution(N: int) -> str:
    prime_list = list(set(find_prime(N)))
    for i in list(prime_list):
        if i%10 != 3:
            return "NO"
    return "YES"


def find_prime(N: int) -> list:
    for i in range(2, N):
        if N%i == 0:
            val_a = find_prime(i)
            val_b = find_prime(N//i)
            return val_a + val_b

    return [N]


if __name__ == "__main__":
    while True:
        N = int(input())
        if N == -1:
            break

        print(N, solution(N))