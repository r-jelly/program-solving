'''
Level: G5
Time: 23m45s
'''
import sys
from typing import List, Tuple, Any
from collections import deque, defaultdict
input = sys.stdin.readline

def find_start_index(N, indexs):
    is_merged = [False] * N
    for _, j in indexs:
        is_merged[j-1] = True
    return is_merged.index(False) + 1

def solution(names: List[str], indexs: List[Tuple[int, ...]]):
    graph = defaultdict(list)
    for i, j in indexs:
        graph[i].append(j)

    stack = deque([find_start_index(len(names), indexs)])
    while stack:
        cur_idx = stack.pop()
        print(names[cur_idx-1], end='')

        if cur_idx in graph:
            stack.extend(reversed(graph[cur_idx]))

if __name__ == "__main__":
    N = int(input())
    names = [input().strip() for _ in range(N)]
    indexs = [tuple(map(int, input().split())) for _ in range(N-1)]
    solution(names, indexs)

# 그냥 for문으로 돌리면 시간 초과 or 메모리 초과
# 시작 지점을 찾아서 DFS로 푸는 것이 핵심!

""" Linked List 풀이법
import sys; input = lambda: sys.stdin.readline().strip()


N = int(input())
arr = [""] + [input() for _ in range(N)]
nxt = [0] * (N+1)
tail = [*range(N+1)]

head = None
for _ in range(N-1):
    a,b = map(int,input().split())
    nxt[tail[a]] = b
    tail[a] = tail[b]
    head = a

ans = []
for _ in range(N):
    ans.append(arr[head])
    head = nxt[head]

print("".join(ans))
"""