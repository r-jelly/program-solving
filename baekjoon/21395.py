'''
Level: S1
Time: 19m17s
'''
import sys
input = sys.stdin.readline

def is_prime(num):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True


def get_prime_nums(max_num=100000):
    return [num for num in range(2, max_num+1) if is_prime(num)]


def solution(N, nums, prime_nums):
    min_cnt = float('inf')
    for i in range(0, len(prime_nums)-N):
        cur_min_cnt = sum([abs(nums[j]-prime_nums[i+j]) for j in range(N)])
        min_cnt = min(cur_min_cnt, min_cnt)
    return min_cnt


if __name__ == "__main__":
    T = int(input())
    prime_nums = get_prime_nums()

    for _ in range(T):
        N = int(input())
        nums = list(map(int, input().split()))
        print(solution(N, sorted(nums), prime_nums))