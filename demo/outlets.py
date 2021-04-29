N = int(input())
c = 0
e = 0

for i in range(N):
    a = int(input())
    if a == 0:
        e += 1
    c += a

print(c - (N - e - 1))
