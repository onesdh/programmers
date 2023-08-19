import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
N, M= map(int, input().split()) # N = x M = Y
# dfs - > 재귀 or stack
# bfs - > queue
# 그래프 생성
graph = [list(input()) for _ in range(N)] 
cnt = 0

# dfs
def dfs(x, y) :
    global cnt
    letter = graph[y][x]
    graph[y][x] = 0
    if letter == '-' :
        if x+1 < M  and graph[y][x+1] == '-':
            dfs(x+1, y)
        else :
            cnt += 1
            return 
    if letter == '|' :
        if y+1 < N  and graph[y+1][x] == '|':
            dfs(x, y+1)
        else :
            cnt += 1
            return 

for i in range(M) :
    for j in range(N) : 
        if graph[j][i] != 0 :      
            dfs(i, j)
print(cnt)

