'''
Level: G3
Time: 46m13s
'''

import sys
import heapq
from collections import defaultdict

def solution(request_dict):
    accept_requests = []

    # 제일 마감기한이 빠른 요청부터 처리
    for day in sorted(request_dict.keys()):
        # 특정 마감기한 day에 대해 비싼 pay부터 받을지 결정
        for pay in sorted(request_dict[day], reverse=True):
            # 만약 현재 마감기한 날짜보다 더 적은 개수의 강연을 하기로 했다면, 해당 강연은 하는 것이 이득
            if len(accept_requests) < day:
                heapq.heappush(accept_requests, pay)
            # 만약 현재 마감기한 날짜만큼 강연을 하기로 했다면, 강연료를 비교해서 더 많은 강연료를 주는 강연을 채택
            elif accept_requests[0] < pay:
                heapq.heappop(accept_requests)
                heapq.heappush(accept_requests, pay)
    return sum(accept_requests)


if __name__ == "__main__":    
    N = int(sys.stdin.readline())

    # {강연 마감일: [강연료_1, 강연료_2, ...], ...}
    request_dict = defaultdict(list)
    for _ in range(N):
        pay, day = list(map(int, sys.stdin.readline().split()))
        request_dict[day].append(pay)

    answer = solution(request_dict)
    sys.stdout.write(f"{answer}")
