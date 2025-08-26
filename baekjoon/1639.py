'''
Level: Silver4
'''
S = input()

def check_lucky(s1: str, s2: str):
    cnt1 = sum([int(s) for s in s1])
    cnt2 = sum([int(s) for s in s2])
    return cnt1 == cnt2

def solution(S: str):
    for i in reversed(range(1, len(S)//2+1)):
        for j in range(len(S)-i*2+1):
            if check_lucky(S[j:j+i], S[j+i:j+2*i]):
                return i*2
    return 0

print(solution(S))