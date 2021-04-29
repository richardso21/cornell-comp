N, K, M = map(int, input().split())
cups = [chr(i) for i in range(97, N + 97)]

seq = input()

# fooled = False

# def lastUnique(seq, t):
#     if t < 0:
#         return 0
#     cupsD = cups.copy()
#     for i, char in enumerate(seq, 1):
#         if char in cupsD:
#             cupsD.remove(char)
#             if len(cupsD) == 0:
#                 return i + max(lastUnique(seq[i-1:], t - 1) - 1, 0)
#     global fooled
#     fooled = True
#     return i

# res = lastUnique(seq, K)

# if fooled:
#     print(-1)
# else:
#     print(res)

s = seq
times = K
res = 0
fooled = False

while len(s) > 0:
    broken = False
    if times < 0:
        break
    cupsD = cups.copy()
    for i, char in enumerate(s, 1):
        if char in cupsD:
            cupsD.remove(char)
            if len(cupsD) == 0:
                times -= 1
                res += i
                s = s[i-1:]
                broken = True
                break
    if not broken:
        fooled = True
        break

if fooled:
    print(-1)
else:
    print(res - K)
