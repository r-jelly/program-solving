'''
Level: S2
Time: 06m08s
'''

from collections import deque

def solution(A: int, B: int):
    '''
    solution using queue
    '''
    queue = deque([(A, 1)])
    while queue:
        cur_num, depth = queue.popleft()
        for next_num in [cur_num*2, cur_num*10+1]:
            if next_num == B:
                return depth+1
            elif next_num > B:
                continue

            queue.append((next_num, depth+1))
    return -1


A, B = list(map(int, input().split()))
print(solution(A, B))