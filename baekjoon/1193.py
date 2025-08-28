X = int(input())

idx = 1
while X - idx > 0:
    X -= idx
    idx += 1

if idx % 2:
    print(f"{idx+1-X}/{X}")
else:
    print(f"{X}/{idx+1-X}")
