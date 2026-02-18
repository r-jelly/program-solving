'''
Level: S2
Time: 25m32s
'''
import sys
input = lambda: sys.stdin.readline().strip()

def solution(nums):
    nums = [num if num!=6 else 9 for num in nums]
    nums = sorted(nums, reverse=True)
    subnum1, subnum2 = '', ''

    for num in nums:
        if not subnum1:
            subnum1 += str(num)
        elif not subnum2:
            subnum2 += str(num)
        else:
            add1 = int(subnum1 + str(num)) * int(subnum2)
            add2 = int(subnum1) * int(subnum2 + str(num))
            if add1 > add2:
                subnum1 += str(num)
            else:
                subnum2 += str(num)
    return int(subnum1) * int(subnum2)
    

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        nums = list(map(int, list(input())))
        print(solution(nums))