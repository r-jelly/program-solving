'''
Level: S2
Time: 13m43s
'''
import sys
input = lambda: sys.stdin.readline().strip()

def solution(word: str, candidate_words: list[str], alp_point: dict) -> list[tuple[str, int]]:
    answer = []
    for c_word in candidate_words:
        word_len = 0
        for i in range(len(word)):
            if word[i] == c_word[i]:
                continue

            x1, y1 = alp_point[word[i]]
            x2, y2 = alp_point[c_word[i]]
            word_len += abs(x1-x2) + abs(y1-y2)
        answer.append((c_word, word_len))
    return sorted(answer, key=lambda x: (x[1], x[0]))


if __name__ == "__main__":
    keyboard = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
    alp_point = dict()

    for row, line in enumerate(keyboard):
        for col, alp in enumerate(line):
            alp_point[alp] = (row, col)

    T = int(input())
    for _ in range(T):
        word, I = input().split()
        candidate_words = [input() for _ in range(int(I))]
        answer = solution(word, candidate_words, alp_point)

        for word, word_len in answer:
            print(word, word_len)