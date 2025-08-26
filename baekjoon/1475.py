'''
Level: Silver5
'''
N = input()
counter = [0] * 9

for num in N:
    if num == '9':
        counter[6] += 1
    else:
        counter[int(num)] += 1

counter[6] = counter[6]//2 if counter[6]%2==0 else counter[6]//2+1

print(max(counter))