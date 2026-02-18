'''
Level: S1
Time: 23m19s
'''
import sys
from collections import Counter
from itertools import chain
input = lambda: sys.stdin.readline().strip()

def solution(N, K, numbers):
    num_counts = Counter(numbers)
    all_nums = len(numbers) + 3
        
    max_cases = 0
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            for k in range(j+1, N+1):
                can_select = num_counts[i] + num_counts[j] + num_counts[k] + 3
                cur_cases = (all_nums-can_select)**K * can_select
                if max_cases < cur_cases:
                    max_cases = cur_cases
                    answer = [i, j, k]

    gcd = get_gcd(all_nums**(K+1), max_cases)
    print(max_cases//gcd, all_nums**(K+1)//gcd)
    print(*answer)

def get_gcd(x, y):
    if x%y == 0:
        return y
    return get_gcd(y, x%y)

if __name__ == "__main__":
    N, M, K = list(map(int, input().split()))
    numbers = [list(map(int, input().split())) for _ in range(M-1)]
    numbers = list(chain(*numbers))
    solution(N, K, numbers)
