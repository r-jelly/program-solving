'''
Level: S5
Time: 21m11s
'''
import sys
from typing import List
input = lambda: sys.stdin.readline().strip()

def solution(road_limit: List[List[int]], user_ride: List[List[int]]):
    # 항상 정확하게 100km의 경우만 들어오게 됨
    # 모든 1km 마다 속도를 비교한다면, O(1)의 시간복잡도로 해결할 수 있음

    speed_limit = [0] * 101
    cumulate_length = 1
    for length, speed in road_limit:
        # 각 구간의 길이마다
        for i in range(0, length):
            # 현재까지 지나온 모든 구간의 길이 다음 칸부터 속도를 지정
            speed_limit[i+cumulate_length] = speed
        # 현재까지 지나온 길이를 업데이트
        cumulate_length += length

    user_speed = [0] * 101
    cumulate_length = 1
    for length, speed in user_ride:
        for i in range(0, length):
            user_speed[i+cumulate_length] = speed
        cumulate_length += length

    max_over_speed = 0
    for i in range(1, 101):
        # 같은 인덱스에 존재하는 값끼리 비교했을 때, 최댓값을 구함
        max_over_speed = max(
            max_over_speed,
            user_speed[i] - speed_limit[i]
        )

    return max_over_speed

if __name__ == "__main__":
    # 입출력 처리
    N, M = list(map(int, input().split()))
    road_limit = [list(map(int, input().split())) for _ in range(N)]
    user_ride = [list(map(int, input().split())) for _ in range(M)]
    answer = solution(road_limit, user_ride)
    print(answer)
