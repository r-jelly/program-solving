'''
Level: S3
Time: 15m50s
'''
import sys
input = sys.stdin.readline


def dfs(min_wcf: tuple, cur_wcf: tuple, cities, cnt=0, idx=0):
    if all([i>=j for i, j in zip(cur_wcf, min_wcf)]):
        return cnt
    
    min_cnt = float('inf')
    for i in range(idx+1, len(cities)):
        next_wcf = tuple(prev + cur for prev, cur in zip(cur_wcf, cities[i]))
        cur_cnt = dfs(min_wcf, next_wcf, cities, cnt+1, idx=i)
        min_cnt = min(cur_cnt, min_cnt)

    return min_cnt


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        W, C, F = list(map(int, input().split()))
        cities = [list(map(int, input().split())) for _ in range(N)]

        result = dfs((W, C, F), (0, 0, 0), cities, 0, -1)
        if result != float('inf'):
            print(result)
        else:
            print("game over")

