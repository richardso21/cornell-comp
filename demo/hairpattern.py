from typing import BinaryIO


N, M = map(int, input().split())

startMatrix = []
targetMatrix = []

def binaryify(l):
    return 1 if l == 'W' else 0

for i in range(N):
    startMatrix.append(list(map(binaryify,list(input()))))

for i in range(N):
    targetMatrix.append(list(map(binaryify,list(input()))))

print(startMatrix)