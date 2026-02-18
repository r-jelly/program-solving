'''
Level: G3
Time: 1h06m34s
'''
import sys
input = lambda: sys.stdin.readline().strip()

def find_primes(max_num=150):
    primes = []
    for num in range(2, max_num+1):
        for i in range(2, num//2+1):
            if num%i==0:
                break
        else:
            primes.append(num)
    return primes

def dfs(N, primes, cur_idx, cur_primes, cur_sq_sum):
    if len(cur_primes) == N:
        if len(set(cur_primes)) == 1:
            return []
        if all(cur_sq_sum % i == 0 for i in cur_primes):
            return cur_primes
        else:
            return []

    for idx in range(cur_idx, len(primes)):
        cur_prime = primes[idx]
        
        cur_primes.append(cur_prime)
        cur_sq_sum += cur_prime**2

        answer = dfs(N, primes, idx, cur_primes, cur_sq_sum)
        if answer:
            return answer

        cur_primes.pop()
        cur_sq_sum -= cur_prime**2

    return []
    

def solution(N):
    primes = find_primes()
    answer = dfs(N, primes, 0, [], 0)
    return answer if answer else [-1]

if __name__ == "__main__":
    N = int(input())

    if N == 5 or N >= 7:
        if N % 2 == 1:
            answer = [2]*3 + [3]*(N-3)
        else:
            answer = [2]*6 + [3]*(N-6)
    else:
        answer = solution(N)

    print(*answer)