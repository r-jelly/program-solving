'''
Level: S2
Time: 11m29s
'''

import sys
input = sys.stdin.readline

def dfs(sizes, cur_sum, cur_idx):
    if cur_sum > 1.01:
        return 0

    cnt = 0
    for i in range(cur_idx+1, len(sizes)):
        cur_sum += sizes[i]
        if 0.99 <= cur_sum <= 1.01:
            cnt += 1

        cnt += dfs(sizes, cur_sum, i)
        cur_sum -= sizes[i]
    return cnt


def solution(sizes: list[int]) -> int:
    float_sizes = [1/size for size in sizes]
    return dfs(float_sizes, 0, -1)


if __name__ == "__main__":
    N = int(input())
    sizes = list(map(int, input().split()))

    print(solution(sorted(sizes)))
