h, w, l, c = map(int, input().split())

def ifFits(h, w, l, c):
    vol = h * w * l
    if vol > c:
        return "SO MUCH SPACE"
    elif vol < c:
        return "TOO TIGHT"
    return "COZY"

print(ifFits(h, w, l, c))