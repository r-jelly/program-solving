'''
Level: S2
Time: 
'''
import sys
input = lambda: sys.stdin.readline().strip()

def solution(time1, time2, interval1, interval2):
    print(time1, interval1)
    print(time2, interval2)

if __name__ == "__main__":
    time1 = list(map(int, input().split(":")))
    time2 = list(map(int, input().split(":")))
    interval1 = list(map(int, input().split(":")))
    interval2 = list(map(int, input().split(":")))

    time1 = time1[0]*60 + time1[1]
    time2 = time2[0]*60 + time2[1]
    interval1 = interval1[0]*60 + interval1[1]
    interval2 = interval2[0]*60 + interval2[1]

    solution(time1, time2, interval1, interval2)