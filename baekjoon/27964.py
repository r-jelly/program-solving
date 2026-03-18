'''
Level: S5
Time: 04m44s
'''
import sys
from typing import List
input = lambda: sys.stdin.readline().strip()

def solution(toping_list: List[str]):
    count = 0
    for toping in toping_list:
        if toping.endswith("Cheese"):
            count += 1
    
    if count >= 4:
        return True
    else:
        return False

if __name__ == "__main__":
    N = int(input())
    toping_list = input().split()
    answer = solution(list(set(toping_list)))
    if answer:
        print("yummy")
    else:
        print("sad")