'''
Level: S5
Time: 21m04s
'''
import sys
input = lambda: sys.stdin.readline().strip()

grades = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0
}

if __name__ == "__main__":
    N, X = input().split()
    all_credit = 0
    cur_point = 0
    for _ in range(int(N)-1):
        c, g = input().split()
        all_credit += int(c)
        cur_point += int(c) * grades[g]

    L = int(input())
    for grade, point in reversed(grades.items()):
        if L * point + cur_point >= (all_credit + L) * (float(X) + 0.01):
            print(grade)
            break
    else:
        print('impossible')