'''
Level: S3
Time: 13m01s
'''
import sys
input = lambda: sys.stdin.readline().strip()

def get_nearest_palindrom(num_str):
    mid_idx = (len(num_str)-1) // 2
    cur_left = list(num_str[:mid_idx+1])
    cur_palindrom = '0'

    while int(cur_palindrom) < int(num_str):
        if len(num_str)%2==0:
            cur_palindrom = ''.join(cur_left) + ''.join(reversed(cur_left))
        else:
            cur_palindrom = ''.join(cur_left) + ''.join(reversed(cur_left[:-1]))

        cur_left = list(str(int(''.join(cur_left)) + 1))
        if len(cur_left) <= mid_idx:
            cur_left = ['0']*(mid_idx-len(cur_left)+1) + cur_left
    return cur_palindrom


if __name__ == "__main__":
    while True:
        num_str = input()
        if '0' == num_str:
            break

        nearest_palindrom = get_nearest_palindrom(num_str)
        print(int(nearest_palindrom) - int(num_str))