'''
Level: S4
Time: 08m23s
'''
import sys
from typing import List
input = lambda: sys.stdin.readline().strip()

def solution(word_list: List[str]):
    word_set = set()
    for word in word_list:
        sorted_word = ''.join(sorted(list(word)))
        if sorted_word in word_set:
            continue
        word_set.add(sorted_word)

    return len(word_set)

if __name__ == "__main__":
    N = int(input())
    word_list = [input() for _ in range(N)]
    answer = solution(word_list)
    print(answer)
