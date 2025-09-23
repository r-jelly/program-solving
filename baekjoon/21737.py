'''
Level: S1
Time: 23m12s
'''

import sys
input = sys.stdin.readline

def parse_sequence(seq):
    parsed = []
    num = []
    for c in seq:
        if c in 'SMUPC':
            if num:
                parsed.append(int(''.join(num)))
                num = []
            parsed.append(c)
        else:
            num.append(c)
    return parsed


def solution(seq, N):
    results = []

    cur_cal = seq[0]
    for i in range(1, len(seq)):
        if seq[i] == "C":
            results.append(cur_cal)

        elif i < len(seq)-1:
            if seq[i] == "S":
                cur_cal -= seq[i+1]
            elif seq[i] == "M":
                cur_cal *= seq[i+1]
            elif seq[i] == "P":
                cur_cal += seq[i+1]
            elif seq[i] == 'U':
                if cur_cal > 0:
                    cur_cal //= seq[i+1]
                else:
                    cur_cal = -(-cur_cal // seq[i+1])

    return results


if __name__ == "__main__":
    N = int(input())
    seq = list(input().strip())
    
    parsed = parse_sequence(seq)
    result = solution(parsed, N)

    if result:
        print(*result)
    else:
        print("NO OUTPUT")