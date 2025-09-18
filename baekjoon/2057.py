'''
Level: S5
Time: 13m28s
'''

import sys
input = sys.stdin.readline

def solution(N):
    if N==0:
        return "NO"
    
    facts = [1, 1]
    for i in range(2, 20):
        facts.append(facts[i-1] * i)

    for i in reversed(range(20)):
        if N >= facts[i]:
            N -= facts[i]

    if N==0:
        return "YES"
    else:
        return "NO"
    

if __name__ == "__main__":
    N = int(input())
    print(solution(N))