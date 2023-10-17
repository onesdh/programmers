import sys
input = sys.stdin.readline

N = int(input())
num = [1, 5, 10, 50]
li = []
for i in range(N+1):
    for j in range(N+1 - i):
        for k in range(N+1 - i - j):
            t = N-i-j-k
            tmp = i*num[0] + j*num[1] + k*num[2]  + t*num[3]
            li.append(tmp)

answer = set(li)
print(len(answer))