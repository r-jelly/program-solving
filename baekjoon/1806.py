import sys

def get_presum_length(nums, presum_list, target):
    if pre_sum[-1] < target:
        return 0
    
    left, right = 0, len(presum_list)-1
    while left <= right:
        cur_sum = presum_list[right+1] - presum_list[left]
        if cur_sum < S:
            return right - left + 1
        
        if nums[left] < nums[right]:
            left += 1
        else:
            right -= 1
    return 1


N, S = list(map(int, sys.stdin.readline().split()))
nums = list(map(int, sys.stdin.readline().split()))
pre_sum = [0]*(N+1)

for i in range(N):
    pre_sum[i+1] = pre_sum[i] + nums[i]

left, right = 0, N-1
while left<=right:
    cur_sum = pre_sum[right+1] - pre_sum[left]
    if cur_sum < S:
        break

    if nums[left] < nums[right]:
        left += 1
    else:
        right -= 1

if left == 0 and right == N-1:
    print(0)
else:
    print(right-left+1)