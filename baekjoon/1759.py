'''
Level: G5
Time: 10m52s
'''
import sys
from typing import List
input = lambda: sys.stdin.readline().strip()

def dfs(L: int, alp_list: List[str], cur_password: List[str], cur_idx: int, count_vowel: int):
    if len(cur_password) == L:
        if count_vowel>=1 and (L-count_vowel)>=2:
            print(''.join(cur_password))
        return
    
    for idx in range(cur_idx+1, len(alp_list)):
        cur_alp = alp_list[idx]

        if cur_alp in ['a', 'e', 'i', 'o', 'u']:
            next_count_vowel = count_vowel + 1
        else:
            next_count_vowel = count_vowel

        cur_password.append(cur_alp)
        dfs(L, alp_list, cur_password, idx, next_count_vowel)
        cur_password.pop()
    return


def solution(L: int, alp_list: List[str]):
    dfs(L, alp_list, [], -1, 0)


if __name__ == "__main__":
    L, C = list(map(int, input().split()))
    alp_list = input().split()
    solution(L, sorted(alp_list))
