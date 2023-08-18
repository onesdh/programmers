import sys
from collections import deque
input = sys.stdin.readline

N, M, R = map(int, input().split()) # n : 정점의 수 M : 간선의 수 R : 시작전점
visit = [0]*(N+1)
answer = [0]*(N+1)
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

# bfs
def bfs(start) :
    global cnt
    queue = deque()
    queue.append(start)
    visit[start] = 1
    answer[start] = cnt
    graph[start].sort(reverse=False)
    # print("queue: ", queue)
    while queue: # queue가 비어있기 전까지 작동 None이되면 작동 정지
        a = queue.popleft()
        # print("pop : ", a)
        graph[a].sort(reverse=False)
        for i in graph[a] :
            # print("i", i , "graph", graph[a])
            if visit[i] == 0 :
                cnt += 1
                visit[i] = 1
                answer[i] = cnt
                queue.append(i)
                #print("queue: ", queue)
bfs(R)
for i in range(1, N+1):
    print(answer[i])

    