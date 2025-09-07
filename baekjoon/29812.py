'''
Level: S5
Time: 24m32s
'''

N = int(input())
S = input()
D, M = list(map(int, input().split()))

energy = 0
no_str = ""
count = {'H': 0, 'Y': 0, 'U': 0}
for i, s in enumerate(S):
    if s in ['H', 'Y', 'U']:
        if no_str:
            energy += M+D if M+D < D*len(no_str) else D*len(no_str)
            no_str = ''
        count[s] += 1
    else:
        no_str += s
else:
    if no_str:
        energy += M+D if M+D < D*len(no_str) else D*len(no_str)
        no_str = ''

if energy == 0:
    print("Nalmeok")
else:
    print(energy)

if min(count.values()) == 0:
    print('I love HanYang University')
else:
    print(min(count.values()))