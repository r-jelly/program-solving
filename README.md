# 코딩테스트 대비용 알고리즘 문제 풀이

세 개의 소스를 하나의 git repo로 통합한 저장소다. (remote: `program-solving`)

- 백준: https://boj.kr
- 프로그래머스: https://programmers.co.kr
- LeetCode: https://leetcode.com

## 통합된 소스

1. **코드 (정본)** — 기존 `program_solving` git repo. `baekjoon/<num>.py`, `leetcode/<num>.py`.
2. **회고 노트** — Obsidian `study/problem_solving`의 문제별 회고 `.md`를 코드 옆에 co-locate(복사)했다. 원본은 Obsidian에 그대로 유지된다.
3. **데일리 STAR 트랙** — `sustainable-life`의 `leetcode` 트랙(README·TEMPLATE·`YYYYMMDD-*.md`)을 `interview-daily/`로 옮겼다.

## 폴더 규칙

- `baekjoon/` — 문제별 `<num>.py`(풀이 코드) + `<num>.md`(회고 노트, Obsidian에서 복사). 노트만 있고 코드가 없는 경우도 있다.
- `leetcode/` — 위와 동일하게 `<num>.py` + `<num>.md`.
- `programmers/` — 아직 README뿐인 빈 껍데기.
- `interview-daily/` — `sustainable-life` STAR 트랙의 **라이브 심볼릭 대상**이다. 옛 경로
  `~/Documents/Claude/Projects/sustainable-life/leetcode`가 이 폴더를 가리키는 심볼릭 링크로 연결돼 있어,
  둘 중 어느 쪽에서 작업해도 같은 파일이다.

## 데일리 풀이 작성법

매일 풀이는 옛 `sustainable-life/leetcode` 경로 또는 이 repo의 `interview-daily/`에 **직접 작성**하면 된다
(심볼릭 링크로 연결되어 있으므로 결과는 동일). 템플릿은 `interview-daily/TEMPLATE.md` 참고.

## 참고

- Obsidian 회고 노트의 `[[wikilink]]`는 repo 밖에서는 링크가 풀리지 않지만 텍스트로 보존돼 있다.
- 회고 노트 파일명은 원본의 `BOJ <num> - <title>` / `Leetcode <num> - <title>` 형식에서 `<num>.md`로 정규화했다.
