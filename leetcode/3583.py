from collections import Counter
class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        left_count = Counter()
        right_count = Counter(nums)

        answer = 0
        for j in range(0, len(nums)):
            right_count[nums[j]] -= 1
            answer += left_count[nums[j]*2] * right_count[nums[j]*2]
            left_count[nums[j]] += 1

        return answer % (10**9 + 7)