'''
Level: S3
Time: 11m37s
'''
import sys
input = lambda: sys.stdin.readline().strip()

def solution(num_list: list[int], x: int) -> int:
    # 시간 초과 -> O(n^2)
    answer = 0
    for i in range(len(num_list)):
        for j in range(i+1, len(num_list)):
            if num_list[i]+num_list[j] == x:
                answer += 1

    return answer

def solution_2(num_list: list[int], x: int) -> int:
    answer = 0

    num_list = sorted(num_list) # 오름차순 정렬 O(N logN)
    left, right = 0, len(num_list)-1

    while left < right: # O(N)
        if num_list[left] + num_list[right] == x:
            answer += 1
            left += 1
            right -= 1
        elif num_list[left] + num_list[right] < x:
            left += 1
        else:
            right -= 1
    return answer


if __name__ == "__main__":
    n = int(input())
    num_list = list(map(int, input().split()))
    x = int(input())

    print(solution_2(num_list, x))