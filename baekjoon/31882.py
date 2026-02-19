'''
Level: S4
Time: 23m56s
'''
import sys
input = lambda: sys.stdin.readline().strip()

def solution(N: int, S: str) -> int:
    answer = 0
    cont_two = 0

    for num in S:
        num = int(num)
        if num != 2:
            if cont_two != 0:
                answer += cont_two * (cont_two+1) * (cont_two+2) // 6
            cont_two = 0
        else:
            cont_two += 1
    else:
        answer += cont_two * (cont_two+1) * (cont_two+2) // 6

    return answer


if __name__ == "__main__":
    N = int(input())
    S = input()
    print(solution(N, S))