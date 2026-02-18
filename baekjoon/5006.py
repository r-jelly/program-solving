'''
Level: S2
Time: 15m10s
'''
import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def solution(N, horror_list, sim_dict):
    horror_indexs = [0 if i in horror_list else float('inf') for i in range(N)]
    queue = deque(horror_list)
    while queue:
        cur_idx = queue.popleft()
        for next_idx in sim_dict[cur_idx]:
            if horror_indexs[next_idx] != float('inf'):
                continue
            horror_indexs[next_idx] = horror_indexs[cur_idx] + 1
            queue.append(next_idx)
    return horror_indexs


if __name__ == "__main__":
    N, H, L = list(map(int, input().split()))
    horror_list = list(map(int, input().split()))
    sim_dict = defaultdict(list)
    for i in range(L):
        a, b = list(map(int, input().split()))
        sim_dict[a].append(b)
        sim_dict[b].append(a)

    horror_indexs = solution(N, horror_list, sim_dict)
    print(horror_indexs.index(max(horror_indexs)))