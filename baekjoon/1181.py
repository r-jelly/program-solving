'''
Level: S5
Time: 10m09s
'''

import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    words = list(set([input().strip() for _ in range(N)]))
    words = sorted(words, key=lambda x: (len(x), x))

    for word in words:
        print(word)