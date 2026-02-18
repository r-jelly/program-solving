'''
Level: S5
Time: 10m20s
'''
import sys
input = lambda: sys.stdin.readline().strip()

def solution(X, C, logs):
    students = [-1] * (X+1)
    seats = [False] * (C+1)
    for t, s, n in logs:
        if seats[s]:
            continue

        if students[n] != -1:
            seats[students[n]] = False
        students[n] = s
        seats[s] = True

    for i, student in enumerate(students):
        if student == -1:
            continue
        print(i, student)
            


if __name__ == "__main__":
    X, C, K = list(map(int, input().split()))
    logs = [list(map(int, input().split())) for _ in range(K)]

    solution(X, C, sorted(logs, key=lambda x: x[0]))