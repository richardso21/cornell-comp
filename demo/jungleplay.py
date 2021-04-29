N, K, M = map(int, input().split())
cups = [chr(i) for i in range(97, N + 97)]

seq = list(input())

def junglePlay(s, t):
    knocked = 0
    if t < 0:
        return 0
    t -= 1
    cupsD = cups.copy()
    for i in s:
        knocked += 1
        if i in cupsD:
            cupsD.remove(i)
            if len(cupsD) == 0:
                return knocked + junglePlay(s[knocked:], t)
    return knocked

t = K
res = junglePlay(seq, t)
if res == M:
    res = -1
else:
    res -= K

print(res)

# knocked = 0
# times = K + 1
# while (times > 0):
#     s = seq[knocked:]
#     use up distraction
#     times -= 1
#     cupsD = cups
#     for i in s:
#         knocked += 1
#         if i in cupsD:
#             if len(cupsD) == 1:
#                 break
#             cupsD.remove(i)

# if knocked == M:
#     knocked = -1
# else:
#     knocked -= K

# print(knocked)