'''
Level: S1
Time: 12m16s
'''
import sys
from typing import Dict, List
from collections import defaultdict
input = lambda: sys.stdin.readline().strip()

def dfs(graph, visited, start):
    stack = [start]
    count = 1

    while stack:
        cur_num = stack.pop()
        for next_num in graph[cur_num]:
            if visited[next_num]:
                continue

            visited[next_num] = True
            stack.append(next_num)
            count += 1
    return count


def solution(N: int, graph: Dict[int, List]):
    visited = [False] * (N+1)
    size = 1
    for i in range(1, N+1):
        if visited[i]:
            continue
        
        visited[i] = True
        cur_size = dfs(graph, visited, i)
        size *= cur_size % 1000000007
    return size % 1000000007


if __name__ == "__main__":
    N, M = list(map(int, input().split()))
    graph = defaultdict(list)

    for _ in range(M):
        u, v = list(map(int, input().split()))
        graph[u].append(v)
        graph[v].append(u)

    answer = solution(N, graph)
    print(answer)