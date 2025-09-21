'''
Level: S3
Time: 22m42s
'''

import sys
input = sys.stdin.readline


def get_min_flip(pancakes: str) -> int:
    stack = list(reversed(pancakes))

    flip_cnt = 0
    while True:
        flag = stack.pop()
        
        cont_cnt = 1
        while stack and stack[-1] == flag:
            stack.pop()
            cont_cnt += 1

        if cont_cnt == len(pancakes) and flag == '+':
            break

        for _ in range(cont_cnt):
            stack.append('+' if flag=='-' else '-')
        flip_cnt += 1

    return flip_cnt


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        line = input().strip()
        num_flip = get_min_flip(line)
        print(f"Case #{i+1}: {num_flip}")