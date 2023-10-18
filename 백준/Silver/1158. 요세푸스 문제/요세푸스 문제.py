import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())
queue = deque([i for i in range(1,N+1)])
answer = []

while queue:
    for _ in range(K-1):
        queue.append(queue.popleft())
    answer.append(queue.popleft())
answer = '<' + ', '.join(map(str, answer)) + '>'

print(answer)