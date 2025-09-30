'''
Level: S1
Time: 26m41s
'''

import sys
from collections import deque
input = sys.stdin.readline


def solution(trucks: deque, W, L):
    first_truck = trucks.popleft()
    
    bridge = deque([0] * (W-1) + [first_truck])
    bridge_l = first_truck
    time = 1

    while bridge:
        cur_out = bridge.popleft()
        bridge_l -= cur_out
        if trucks:
            if bridge_l + trucks[0] > L:
                bridge.append(0)
            else:
                cur_in = trucks.popleft()
                bridge.append(cur_in)
                bridge_l += cur_in
        time += 1
    return time


if __name__ == '__main__':
    N, W, L = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    print(solution(deque(trucks), W, L))
