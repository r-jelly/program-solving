'''
Level: S2
Time: 11m10s
'''
import sys
input = lambda: sys.stdin.readline().strip()

if __name__ == "__main__":
    cursor_left = list(input())
    cursor_right = []
    N = int(input())

    for _ in range(N):
        argv = input().split()
        if argv[0] == 'L':
            if not cursor_left:
                continue
            cursor_right.append(cursor_left.pop())
        elif argv[0] == 'D':
            if not cursor_right:
                continue
            cursor_left.append(cursor_right.pop())
        elif argv[0] == 'B':
            if not cursor_left:
                continue
            cursor_left.pop()
        else:
            cursor_left.append(argv[1])
    print(''.join(cursor_left) + ''.join(reversed(cursor_right)))