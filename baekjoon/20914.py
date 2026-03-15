'''
Level: S2
Time: 20m52s
'''
import sys
from collections import deque
input = lambda: sys.stdin.readline().strip()

def find_min_time(keyboard, src, tgt):
    visited = [[False]*10 for _ in range(3)]
    visited[src[0]][src[1]] = True

    queue = deque([(src, 0)])
    while queue:
        (cur_x, cur_y), time = queue.popleft()
        if cur_x == tgt[0] and cur_y == tgt[1]:
            return time

        for dx, dy in [(1, 0), (-1, 0), (0, -1), (0, 1), (-1, 1), (1, -1)]:
            next_x = cur_x + dx
            next_y = cur_y + dy

            if next_x<0 or next_x>=3:
                continue
            if next_y<0 or next_y>=len(keyboard[next_x]):
                continue
            if visited[next_x][next_y]:
                continue

            visited[next_x][next_y] = True
            queue.append(((next_x, next_y), time+2))


def solution(keyboard, word):
    time = 0
    word_point_list = []

    for alp in word:
        for i in range(len(keyboard)):
            for j in range(len(keyboard[i])):
                if keyboard[i][j] == alp:
                    word_point_list.append((i, j))

    for i in range(len(word)-1):
        time += 1
        time += find_min_time(keyboard, word_point_list[i], word_point_list[i+1])
    return time+1


if __name__ == "__main__":
    keyboard = ['QWERTYUIOP', 'ASDFGHJKL', 'ZXCVBNM']
    T = int(input())
    for _ in range(T):
        word = input()
        answer = solution(keyboard, word)
        print(answer)