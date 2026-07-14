'''
Level: G4
Time:
'''
import sys
from typing import List
from collections import deque
input = lambda: sys.stdin.readline().strip()

def bfs(graph, is_cycle, num):
    visited = [0] * (len(graph)+1)
    visited[num] += 1
    is_cycle[num] = -1
    queue = deque([num])

    while queue:
        cur_num = queue.popleft()
        next_num = graph[cur_num-1] 

        if visited[next_num] >= 2:
            continue

        visited[next_num] += 1
        queue.append(next_num)

        if visited[next_num] == 1:
            is_cycle[next_num] = -1
        elif visited[next_num] == 2:
            is_cycle[next_num] = 1


def solution(graph):
    is_cycle = [0] * (len(graph)+1)
    for i in range(1, len(graph)+1):
        if is_cycle[i]:
            continue

        bfs(graph, is_cycle, i)



if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        graph = list(map(int, input().split()))
        answer = solution(graph)
        print(answer)