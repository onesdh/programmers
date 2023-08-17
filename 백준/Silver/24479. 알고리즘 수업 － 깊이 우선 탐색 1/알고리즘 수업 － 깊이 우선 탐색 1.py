import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
N, M, R = map(int, input().split()) # n : 정점의 수 M : 간선의 수 R : 시작전점
visit = [0]*(N+1)

cnt = 1
# dfs - > 재귀 or stack
# bfs - > queue
# 그래프 생성
graph = [[] for _ in range(N+1)]

for _ in range(M) :
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    
    
#[[], [4, 2], [1, 3, 4], [2, 4], [1, 2, 3], []] 이러한 형식으로 graph 출력 sort 필요

# for i in range(1, len(graph)):
#     graph[i].sort(reverse=False)

#print(graph)

# dfs
def dfs(start) :
    global cnt 
    visit[start] = cnt
    graph[start].sort(reverse=False)
    for i in graph[start] :
        if visit[i] == 0 :
            cnt += 1
            #print(visit)
            #print(cnt)
            dfs(i)
dfs(R)
for i in range(1, N+1):
    print(visit[i])

    