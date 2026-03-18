'''
Level: S4
Time: 07m54s
'''
import sys
from typing import List
input = lambda: sys.stdin.readline().strip()

def gcd(x: int, y: int) -> int:
    assert x <= y
    if y%x == 0:
        return x
    return gcd(y%x, x)

def solution(num_list: List[int]) -> int:
    answer = 0
    for i in range(1, len(num_list)):
        for j in range(i+1, len(num_list)):
            answer += gcd(min(num_list[i], num_list[j]), max(num_list[i], num_list[j]))
    return answer

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        num_list = list(map(int, input().split()))
        answer = solution(num_list)
        print(answer)