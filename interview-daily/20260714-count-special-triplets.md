# 3583 — Count Special Triplets

- **날짜:** 2026-07-14
- **링크:** https://leetcode.com/problems/count-special-triplets/
- **난이도:** Medium

## 풀이

```python
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
```

## S — Situation (문제가 뭔가)
정수 배열 `nums`가 주어졌을 때, `nums[i]==nums[k]==nums[j]*2`를 만족하는 `i<j<k`를 찾는다. 이때, `nums.length`는 최대 `10^5`이고 결과가 클 수 있으므로 최종 반환시 `10^9+7`로 modulo 연산을 수행해야 한다.

## T — Task (왜 까다로웠나)
우선적으로 모든 (i, j, k)를 확인하는 Brute force 기법은 O(N^3)이고, j를 고정하고 모든 가능한 i와 k 각각을 세는 기법도 O(N^2)이었다. 이때 N=10^5이므로 해당 시간복잡도에서는 1초 안에 해결하기 어렵다.
이때 j를 고정하는 것이 시간복잡도를 감소하는데, j를 고정하게 되면 j 왼쪽에서 조건에 해당하는 값의 개수를 알고, j 오른쪽에서 조건에 해당하는 값의 개수를 알아서 해당 값들을 곱하게 된다면 해당 j에서의 가능한 triplet 수가 되는 것이다. 즉 j를 고정하면 굳이 i, k 각각을 매번 셀 필요가 없다.

## A — Action (접근과 대안)
- **검토한 대안들:**
  1. Brute force: O(N^3), 구현 단순
  2. j를 고정하고 i, k를 매번 반복 탐색: O(N^2), 추가 메모리 필요 없음
  3. 정렬 기반: j 좌우 리스트를 만들어 정렬해서 값을 찾는 방식
  4. 해시맵 기반: j 왼쪽/오른쪽 값의 개수를 dictionary로 세어 O(1) 조회
- **각 대안의 트레이드오프:** 정렬 기반 방식은 j가 변할 때마다 좌우 리스트를 새로 정렬해야 하는 문제가 있다. 해시맵 기반 방식은 각 숫자의 개수를 미리 세어놓고 j가 이동함에 따라 값을 변동시키기만 하면 되므로 시간복잡도 측면에서 이득이다.
- **최종 선택과 근거:** 해시맵 기반 방식 선택. 전체 배열을 한 번만 순회하며, 값 저장·탐색이 O(1)이다. `left_count`는 j 왼쪽 값들의 개수, `right_count`는 j 오른쪽 값들의 개수를 유지한다.
  - **핵심 invariant:** `right_count`는 처음에 전체 배열의 값 개수로 초기화되므로, j가 진행됨에 따라 `right_count[nums[j]]`를 먼저 하나 감소시켜야 그 시점에 "j보다 오른쪽"의 개수가 된다. 만약 감소를 `answer` 계산 *뒤에* 했다면, 계산 시점에 `right_count`가 아직 인덱스 j 자신을 포함한 상태라서 틀린다 — 예를 들어 `nums=[0,0,0]`, j=1일 때 감소를 나중에 하면 `right_count[0]`이 1이 아니라 2가 되어 `k=j`를 잘못 세게 된다. 따라서 "감소 먼저, 계산은 그 다음" 순서가 correctness의 핵심이다.

## R — Result (복잡도·한계)
- **시간복잡도:** O(N) — 배열을 한 번만 순회, 딕셔너리 조회/삽입은 평균 O(1)
- **공간복잡도:** O(N) — `left_count`, `right_count`가 최악의 경우 서로 다른 값 전부를 저장
- **Correctness 근거:** `right_count[nums[j]]`를 감소시킨 후에 `answer`를 계산하므로, 그 시점의 `right_count`는 항상 "j보다 엄격히 오른쪽"의 개수를 의미한다. 감소를 계산 뒤로 미루면 j 자신이 포함되어 오답이 나온다(`[0,0,0]` 반례로 확인).
- **엣지케이스:** 배열 길이가 3보다 작은 경우와 중복값(`[0,0,0]` 등)이 있는 경우 모두 별도 처리 없이 동일한 로직으로 올바르게 처리된다.
- **한계:** `i<j<k` 순서 제약이 없었다면 j를 고정해 좌우를 나눌 필요 없이, 전체 값 개수만 구해서 답을 계산하는 방식으로도 충분했을 것이다.

## 3질문 셀프체크
- [x] 뭘 하는가 — 침묵 없이 설명 가능
- [x] 어떻게 동작하는가 — 원리까지 설명 가능
- [x] 장단점·대안 — 트레이드오프 설명 가능
