'''
Level: S4
Time: 02m53s
'''
import sys
input = lambda: sys.stdin.readline().strip()


if __name__ == "__main__":
    K = int(input())
    stack = []
    for _ in range(K):
        num = int(input())
        if num == 0:
            stack.pop()
        else:
            stack.append(num)

    print(sum(stack))