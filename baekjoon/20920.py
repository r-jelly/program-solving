'''
Level: S3
Time: 11m13s
'''
import sys
from collections import defaultdict
input = lambda: sys.stdin.readline().strip()


if __name__ == "__main__":
    N, M = list(map(int, input().split()))
    word_dict = defaultdict(int)
    for _ in range(N):
        word = input()
        if len(word) >= M:
            word_dict[word] += 1


    for word, cnt in sorted(word_dict.items(), key=lambda x: (-x[1], -len(x[0]), x[0])):
        print(word)